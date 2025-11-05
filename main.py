import pygame as py
import sys

py.init()
run = True

WIDTH, HEIGHT = 1080,720

WIN = py.display.set_mode((WIDTH, HEIGHT))

clock = py.time.Clock()

WHITE = (255,255,255)
BLACK = (0, 0, 0)
BLACK = (0, 0, 0)

class Shape():
    
    def __init__(self,fill,border,border_color):
        self.fill = fill
        self.border = border
        self.border_color = border_color

class Rect(Shape):
    
    def __init__(self,x,y,width,height,fill,border=0,border_color=0):
        super().__init__(fill,border,border_color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = py.rect.Rect(x,y,width,height)
    
    def draw(self):
        if self.fill != None:
            py.draw.rect(WIN,self.fill,self.rect)
        
        if self.border > 0:
            py.draw.rect(WIN, self.border_color, self.rect, self.border)

class Elipse(Shape):
    def __init__(self,x,y,width,height,fill,border=0,border_color=0):
        super().__init__(fill,border,border_color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = py.rect.Rect(x,y,width,height)
    
    def draw(self):
        if self.fill != None:
            py.draw.ellipse(WIN,self.fill,self.rect)
        
        if self.border > 0:
            py.draw.ellipse(WIN, self.border_color, self.rect, self.border)

class Poly(Shape):
    def __init__(self,points,fill,border=0,border_color=0):
        super().__init__(fill,border,border_color)
        self.points = points
    
    def draw(self):
        if self.fill != None:
            py.draw.polygon(WIN, self.fill, self.points)
        
        if self.border > 0:
            py.draw.polygon(WIN, self.border_color, self.points, self.border)


class Arc(Shape):
    def __init__(self,x,y,width,height,fill,border=0,thick=0):
        super().__init__(x,y,fill,border,thick)
        self.width = width
        self.height = height

class Line(Shape):
    def __init__(self,x,y,width,height,fill,border=0,thick=0):
        super().__init__(x,y,fill,border,thick)
        self.width = width
        self.height = height

class Button():
    def __init__(self):
        pass


shapes = [Rect(5,5,10,10,(255,0,0), 2, (0,255,0))]

def update():
    WIN.fill((WHITE))
    py.draw.line(WIN, BLACK, (0, 640), (1080,640))

    for shape in shapes:
        shape.draw()


while run:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
            py.quit()
            sys.exit()
    
    update()
    py.display.update()
    clock.tick(30)