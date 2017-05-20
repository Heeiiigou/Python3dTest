import numpy as np

WINDOW_SIZE = (800,600)
BACKGROUND_COLOR = (255,255,255,0)
FLOOR_COLOR = (192/255,192/255,192/255)

verticies = np.array([
    [ 1, -1, -1, 1],
    [ 1,  1, -1, 1],
    [-1,  1, -1, 1],
    [-1, -1, -1, 1],
    [ 1, -1,  1, 1],
    [ 1,  1,  1, 1],
    [-1, -1,  1, 1],
    [-1,  1,  1, 1]
    ])

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

ground_vertices = np.array([
[-10,-0.1,50,1],
[10,-0.1,50,1],
[-10,-0.1,-300,1],
[10,-0.1,-300,1],
])


ground_surfaces = (0,1,2,3)