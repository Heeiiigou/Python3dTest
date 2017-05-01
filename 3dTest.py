import os, sys, pygame
from pygame.locals import *
from Point3D import Point3D
from operator import itemgetter

if not pygame.font: print ("Warning, fonts disabled")
if not pygame.mixer: print ("Warning, sound disabled")

class Test3dMain:
        """Main 3dTest Class"""
        def __init__(self, width=800,height=600, windowName = "Default"):
            """Contructor"""
            pygame.init()
            self.width      = width
            self.height = height
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption("Test3d")
            self.clock = pygame.time.Clock()

            self.vertices = [
                Point3D(-1,1,-1),
                Point3D(1,1,-1),
                Point3D(1,-1,-1),
                Point3D(-1,-1,-1),
                Point3D(-1,1,1),
                Point3D(1,1,1),
                Point3D(1,-1,1),
                Point3D(-1,-1,1)
            ]
            self.faces  = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]
            self.colors = [(255,0,255),(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,0)]
            self.angle  = 0
            pygame.font.init()
            self.fpsfont = pygame.font.SysFont('Comic Sans MS', 30)
        def MainLoop(self):
            """MainLoop"""      
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                
                self.clock.tick(50)
                self.screen.fill((0,32,0))
                textsurface = self.fpsfont.render(str(round(self.clock.get_fps(),2)),False, (0,0,0))
                self.screen.blit(textsurface,(0,0))
                t = []

                for v in self.vertices:
                    # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                    r = v.rotateX(self.angle).rotateY(self.angle).rotateZ(self.angle)
                    # Transform the point from 3D to 2D
                    p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                    # Put the point in the list of transformed vertices
                    t.append(p)
         
                    # Calculate the average Z values of each face.
                avg_z = []
                i = 0
                for f in self.faces:
                    z = (t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0
                    avg_z.append([i,z])
                    i = i + 1
     
                # Draw the faces using the Painter's algorithm:
                # Distant faces are drawn before the closer ones.
                for tmp in sorted(avg_z,key=itemgetter(1),reverse=True):
                    face_index = tmp[0]
                    f = self.faces[face_index]
                    pointlist = [(t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y),
                                 (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y),
                                 (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y),
                                 (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y)]
                    pygame.draw.polygon(self.screen,self.colors[face_index],pointlist)
     
                self.angle += 1
     
                pygame.display.flip()
if __name__ == "__main__":
        MainWindow = Test3dMain()
        MainWindow.MainLoop()