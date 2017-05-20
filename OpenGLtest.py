import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from misc import *
import numpy as np
from object import *

class Camera:
    """Camera functions"""
    def __init__(self, position=(0,0,-5), upVector = (0,1,0), fixPoint = (0,0,0)):
        self.pos = position
        self. upVector = upVector
        self.fixPoint = fixPoint
    def move(self, position=(0,0,0)):
        self.pos = position
        gluLookAt(*self.pos, *self.fixPoint, *self.upVector)
    def moveUp(self,y = 0.5):
        self.pos =(self.pos[0],self.pos[1]+y,self.pos[2])
        gluLookAt(*self.pos,*self.fixPoint,*self.upVector)
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

        gluPerspective(45, (width/height), 0.1, 50.0)
        glTranslatef(0.0,0.0, -5)

        pygame.font.init()
        self.fpsfont = pygame.font.SysFont('Comic Sans MS', 30)

        self.lastTick = 1
        #glClearColor(*BACKGROUND_COLOR)
        self.renderList=[]
        self.renderList.append(Cube())
        self.renderList[0].move((0,1,0))
        self.renderList.append(Ground())
        self.cam = Camera()
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
                    if event.key == pygame.K_LEFT:
                        glTranslatef(-0.5,0,0)
                    if event.key == pygame.K_RIGHT:
                        glTranslatef(0.5,0,0)
                    if event.key == pygame.K_UP:
                        a = self.renderList[0].getPos()
                        self.renderList[0].move((a[0],a[1]+1,a[2]))
                        #glTranslatef(0,-1,0)
                    if event.key == pygame.K_DOWN:
                        a = self.renderList[0].getPos()
                        self.renderList[0].move((a[0],a[1]-1,a[2]))
                        #glTranslatef(0,1,0)
                    if event.key == pygame.K_w:
                        self.cam.moveUp()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0,0,1.0)
                    if event.button == 5:
                        glTranslatef(0,0,-1.0)
    def calcFPS(self):
        """Calculate FPS"""
        ticks = pygame.time.get_ticks() - self.lastTick
        self.lastTick = ticks
        return round(1/ticks/1000,2)

if __name__ == "__main__":
        sim = Simulation()
        sim.mainLoop()