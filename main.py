import pygame as py
import sys

py.init()
run = True

WIDTH, HEIGHT = 1080,720

WIN = py.display.set_mode((WIDTH, HEIGHT))

clock = py.time.Clock()

BLUE = (0, 0, 255)

class Shape():
    
    def __init__(self,x,y,fill,border,thick):
        self.x = x
        self.y = y
        self.fill = fill
        self.border = border
        self.thick = thick

class Rect(Shape):
    
    def __init__(self,x,y,width,height,fill,border=0,thick=0):
        super().__init__(fill,border,thick)
        self.width = width
        self.height = height


def update():
    WIN.fill(BLUE)

while run:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
            py.quit()
            sys.exit()
    
    update()
    py.display.update()
    clock.tick(30)