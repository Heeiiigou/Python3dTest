import numpy as np
from misc import *
from OpenGL.GL import *
from OpenGL.GLU import *
from object import *

class Axis(object):
    def __init__(self):
        self.vertices = axis_vertices
    def render(self):
        glBegin(GL_LINES)
        i = 0
        for edge in axis_edges:
            glColor3fv(axis_edgecolor[i%3])
            i+=1
            for vertex in edge:
                glVertex4fv(self.vertices[vertex])
        glEnd()

class Quad(object):
    def __init__(self):
        self.cube = Cube()
    def render(self):
        self.cube.render()

class Graph(object):
    def __init__(self):
        self.axis = Axis()
        self.axis.scale(1)
        self.quad = Quad()
    def render(self):
        self.axis.render()
        self.quad.render()

