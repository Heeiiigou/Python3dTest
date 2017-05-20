import numpy as np
from misc import *
from OpenGL.GL import *
from OpenGL.GLU import *
class object:
    """Object Model"""
    def render(self):
        print ("default Rendermethod in class", type(self).__name__)
        return
    def move(self, position = (0,0,0)):
        if self.pos == position:
            return
        matrix = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[*self.pos,1]])
        i = 0
        for vertex in self.vertices:
            self.vertices[i] -= np.array([*self.pos,0])
            self.vertices[i] += np.array([*position,0])
            i+=1
        self.pos = position
    def getPos(self):
        return self.pos
    def getRendered(self):
       return self.rendered
    rendered = True
    pos = (0,0,0)
    vertices = np.array([0])

class Cube(object):
    def render(self):
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex4fv(self.vertices[vertex])
        glEnd()
    def __init__(self):
        self.vertices = verticies
    pos = (0,0,0)

class Ground(object):
    def __init__(self):
        self.vertices=ground_vertices
    def render(self):
        glBegin(GL_QUADS)

        x = 0
        for vertex in self.vertices:
            x+=1
            glColor3fv(FLOOR_COLOR)
            glVertex4fv(vertex)
        glEnd()
