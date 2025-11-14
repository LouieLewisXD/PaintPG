# Init
import pygame as py
import sys, math

py.init()

run = True
WIDTH, HEIGHT = 750,500
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("PaintPG")
icon = py.image.load("pencil.png")
py.display.set_icon(icon)

keys_pressed  = []
mouse_pressed = []
mouse_pos = ()
clock = py.time.Clock()

sans_code = py.font.SysFont("Verdana", 20)

# Colors
WHITE = (255,255,255)
BLACK = (0, 0, 0)

# Parent Shape Class
class Shape():

    def __init__(self, shape_drawn, fill, fill_color, border, border_color):
        
        self.shape_drawn = shape_drawn
        self.fill = fill
        self.fill_color = fill_color
        self.border = border
        self.border_color = border_color

# Rectangle Class
class Rect(Shape):

    def __init__(self, shape_drawn=True, x=0, y=0, center=False, width=0, height=0, fill=True, fill_color=BLACK, border=0, border_color=BLACK):
        super().__init__(shape_drawn, fill, fill_color, border, border_color)

        # If cords are for topleft corner
        if not center:
            self.origin = (x, y)
            self.rect = py.Rect(x, y, width, height)
        # If cords are for center
        else:
            self.origin = (x, y)
            self.rect = py.Rect(center=(x,y), width=self.width, height=self.height)

# Ellipse Class
class Ellipse(Shape):

    def __init__(self, shape_drawn=True, x=0, y=0, center=False, width=0, height=0, fill=True, fill_color=BLACK, border=0, border_color=BLACK):
        super().__init__(shape_drawn, fill, fill_color, border, border_color)

        # If cords are for topleft corner
        if not center:
            self.origin = (x, y)
            self.rect = py.Rect(x, y, width, height)
        # If cords are for center
        else:
            self.origin = (x, y)
            self.rect = py.Rect(center=(x,y), width=self.width, height=self.height)

class Polygon(Shape):

    def __init__(self, shape_drawn=True, points=[], fill=True, fill_color=BLACK, border=0, border_color=BLACK):
        super().__init__(shape_drawn, fill, fill_color, border, border_color)

        self.points = []

# loop for all the game functions/drawing
def update():
    WIN.fill(WHITE)

# main game loop
while run:

    for event in py.event.get():

        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            keys_pressed.append(event.key)
        if event.type == py.KEYUP:
            keys_pressed.remove(event.key)
        if event.type == py.MOUSEBUTTONDOWN:
            mouse_pressed.append(event.)            
    print(mouse_pressed)
    update()
    py.display.update()
    clock.tick(60)