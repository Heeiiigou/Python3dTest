import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from misc import *
import numpy as np
from object import *
from graph import *
import math

class Camera:
    """Camera functions"""
    def __init__(self, position=(0,0,-5), upVector = (0,1,0), fixPoint = (0,0,0)):
        self.pos = position
        self. upVector = upVector
        self.fixPoint = fixPoint
        self.x = 0
        self.theta = 1
        self.phi = 0
        self.radius = 100
    def move(self, position=(0,0,0)):
        self.pos = position
        gluLookAt(*self.pos, *self.fixPoint, *self.upVector)
    def moveUp(self,y = 0.5):
        glTranslatef(0,-y, 0)
    def moveDown(self,y = 0.5):
        glTranslatef(0,y, 0)
    def moveForward(self,z = 0.5):
        glTranslatef(0,0, z)
    def moveBackward(self,z = 0.5):
        glTranslatef(0,0, -z)
    def moveRight(self,x = 0.5):
        glTranslatef(-x,0, 0)
    def moveLeft(self,x = 0.5):
        glTranslatef(x, 0, 0)
    def rotateX(self,d = 10.0):
        glRotatef(d,1.0,0.0,0.0)
    def rotateY(self,d = 10.0):
        glRotatef(d,0.0,1.0,0.0)
    def rotateZ(self,d = 10.0):
        glRotatef(d,0.0,0.0,1.0)
    #TODO: conditional Movement with Fixed Point with gluLookAt()


class Simulation:
    """Simulationclass"""
    def __init__(self, width=WINDOW_SIZE[0],height=WINDOW_SIZE[1], caption="Simulation"):
        """Constructor"""
        self.windowWidth = width
        self.windowHeight = height

        pygame.init()
        self.screen = pygame.display.set_mode((self.windowWidth,self.windowHeight), DOUBLEBUF|OPENGL)

        pygame.display.set_caption(caption)

        gluPerspective(45, (self.windowWidth/self.windowHeight), 0.1, 1000.0)
        glTranslatef(0.0,0.0, -5)
        pygame.font.init()
        self.fpsfont = pygame.font.SysFont('Comic Sans MS', 30)

        self.lastTick = 1
        #glClearColor(*BACKGROUND_COLOR)
        self.renderList=[]
        self.renderList.append(Graph())
        self.renderList.append(Cube())
        self.cam = Camera()
        self.mouseDown = 0
    def mainLoop(self):
        while True:
            self.eventHandler()

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            for obj in self.renderList:
                if obj.getRendered():
                    obj.render()
            pygame.display.flip()

    def eventHandler(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    #Rotating with Arrow-Keys
                    if event.key == pygame.K_LEFT:
                        self.cam.rotateY(-10.0)
                    if event.key == pygame.K_RIGHT:
                        self.cam.rotateY(10.0)
                    if event.key == pygame.K_UP:
                        self.cam.rotateX(-10.0)
                    if event.key == pygame.K_DOWN:
                        self.cam.rotateX(10.0)

                    #Move with QEWASD 
                    if event.key == pygame.K_q:
                        self.cam.moveUp()
                    if event.key == pygame.K_e:
                        self.cam.moveDown()
                    if event.key == pygame.K_w:
                        self.cam.moveForward()
                    if event.key == pygame.K_s:
                        self.cam.moveBackward()
                    if event.key == pygame.K_a:
                        self.cam.moveLeft()
                    if event.key == pygame.K_d:
                        self.cam.moveRight()
                    if event.key == pygame.K_r:
                        self.cam.rotate()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print (pygame.mouse.get_pos())
                        if self.mouseDown == 0:
                            self.mouseDown = 1
                            self.clickPos = pygame.mouse.get_pos()
                    if event.button == 4:
                        glTranslatef(0,0,1.0)
                    if event.button == 5:
                        glTranslatef(0,0,-1.0)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.mouseDown = 0
        if self.mouseDown == 1:
            cur = pygame.mouse.get_pos()
            difX = self.clickPos[0] - cur[0]
            difY = self.clickPos[1] - cur[1]
            self.cam.rotateY(-difX)
            self.cam.rotateX(-difY)
            self.clickPos = cur
    def calcFPS(self):
        """Calculate FPS"""
        ticks = pygame.time.get_ticks() - self.lastTick
        self.lastTick = ticks
        return round(1/ticks/1000,2)

if __name__ == "__main__":
        sim = Simulation()
        sim.mainLoop()