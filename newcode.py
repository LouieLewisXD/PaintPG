# Init
import pygame as py
import HelperGUI as GUI
import sys, math

py.init()

run = True
WIDTH, HEIGHT = 750,500
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("PaintPG")
icon = py.image.load("assets\pencil.png")
py.display.set_icon(icon)

keys_pressed  = []
mouse_pressed = []
mouse_pos = ()
released_keys = []
released_mouse = [False,False,False]
clock = py.time.Clock()

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

# Drawing functions


# Drawing variables

brush_size = 5

# All the menu declaration

brush_size_text = GUI.Text("Verdana", 20, str(brush_size), BLACK, midtop=(60,45))
shapes_menu = GUI.Menu(WIN, 120, 200, [], [GUI.ImageButton(None, None, GUI.Image("assets\line.png", topleft=(0, 0))), GUI.ImageButton(None, None, GUI.Image("assets\polygon.png", topleft=(0, 50))), GUI.ImageButton(None, None, GUI.Image("assets\ellipse.png", topleft=(0, 100))), GUI.ImageButton(None, None, GUI.Image("assets\\rectangle.png", topleft=(0, 150)))], [], [], False)
bottom_menu = GUI.Menu(WIN, 0, 400, [GUI.Rect(True, WHITE, 0, None, 0, 0, 750, 100), GUI.Rect(True, BLACK, 0, None, 0, 0, 750, 1)], [GUI.ImageButton(None, None, GUI.Image("assets\pencil.png", midleft=(5,50))), GUI.ImageButton(shapes_menu.toggle, None, GUI.Image("assets\shapes.png", midleft=(105,50))), GUI.ImageButton(None, None, GUI.Image("assets\\floppy_disk.png", midleft=(205,50)))], [], [], True)

# loop for all the game functions/drawing
def update():
    # Functions
    
    if released_mouse[0]:
        bottom_menu.check_buttons(mouse_pos)


    # Drawing
    WIN.fill(WHITE)
    bottom_menu.draw()
    shapes_menu.draw()


# main game loop
while run:

    # resets lists keeping track of released keys/buttons
    released_keys = []
    released_mouse = [False,False,False]
    for event in py.event.get():

        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            keys_pressed.append(event.key)
        if event.type == py.KEYUP:
            keys_pressed.remove(event.key)
            released_keys.append(event.key)
        if event.type == py.MOUSEBUTTONDOWN:
            mouse_pressed = py.mouse.get_pressed()
        if event.type == py.MOUSEBUTTONUP:
            #checks the difference between current pressed and past pressed and adds the released mouse buttons
            current_pressed = mouse_pressed
            mouse_pressed = py.mouse.get_pressed()          
            for mouse_button in range(3):
                if current_pressed[mouse_button] != mouse_pressed[mouse_button]:
                    released_mouse[mouse_button] = True
    
    mouse_pos = py.mouse.get_pos()
    update()
    py.display.update()
    clock.tick(60)