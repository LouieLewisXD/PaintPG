import pygame as py
import sys, math

py.init()
run = True

WIDTH, HEIGHT = 750,500

WIN = py.display.set_mode((WIDTH, HEIGHT))

clock = py.time.Clock()

sans_code = py.font.SysFont("Verdana", 20)

WHITE = (255,255,255)
BLACK = (0, 0, 0)

class Shape():

    shapes_list: bool
    
    def __init__(self, shapes_list=False):
        self.shapes_list = shapes_list

class Rect():

    x: int
    y: int
    width: int
    height: int
    origin: tuple[int,int]
    rect: py.Rect
    fill: bool
    border: bool
    fill_color: tuple[int,int,int]
    border_thickness: int
    border_color: tuple[int,int,int]



    def __init__(x=0,y=0,width=0,height=0,origin=(0,0),rect=py.Rect(),fill=(0,0,0)):
        super.__init__()

class Ellipse():

    def __init__(self):
        super.__init__()

class Circle():

    def __init__(self):
        super.__init__()

class Line():

    def __init__(self):
        super.__init__()

class Polygon():

    def __init__(self):
        super.__init__()