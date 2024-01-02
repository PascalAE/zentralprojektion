import numpy as np
import matplotlib.pyplot as plt

class Parallelepiped:
    def __init__(self, origin, a, b, c):

        self.origin = np.array(origin)
        self.a = np.array(a)
        self.b = np.array(b)
        self.c = np.array(c)

        if not self.check_first_octant_level():
            raise ValueError("not first octant.")

    def check_first_octant_level(self):
        points = [self.origin, self.origin + self.a, self.origin + self.b, self.origin + self.c]
        return all(p[0] >= 0 and p[1] >= 0 and p[2] >= 0 for p in points)
    
    def get_points(self):
        return [
            self.origin,
            self.origin + self.a,
            self.origin + self.b,
            self.origin + self.a + self.b,
            self.origin + self.c,            
            self.origin + self.a + self.c,
            self.origin + self.b + self.c,
            self.origin + self.a + self.b + self.c
        ]

def project_point_xy(point, camera):
    direction = point - camera
    t = -camera[2] / direction[2]
    projected_point = camera + t * direction
    return projected_point[:2]

def plot_parallelepiped_in_xy(parallelepiped, view):
    points = parallelepiped.get_points()

    projected_points = [project_point_xy(p, view) for p in points]

    fig, ax = plt.subplots()
    x, y = zip(*projected_points)
    
    ax.scatter(x, y)
    
    edges = [
        (0, 1), (1, 3), (3, 2), (2, 0),  
        (4, 5), (5, 7), (7, 6), (6, 4),  
        (0, 4), (1, 5), (2, 6), (3, 7)   
    ]

    for start, end in edges:
        ax.plot((x[start], x[end]), (y[start], y[end]), 'b-')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Zentralprojektion XY-Bild')
    plt.grid(True)
    plt.show()

parallelepiped = Parallelepiped([1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1])

view1 = np.array([2, 2, 2])
view2 = np.array([6, 6, 6])
view3 = np.array([5, 5, 10])

plot_parallelepiped_in_xy(parallelepiped, view1)
plot_parallelepiped_in_xy(parallelepiped, view2)
plot_parallelepiped_in_xy(parallelepiped, view3)

