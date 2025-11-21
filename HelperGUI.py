import pygame as py

py.init()

'''
Menu Class - Used to define an area with shapes, buttons, and images
                that can be opened and closed

__init__ -  Declartion of a Menu 
Parameters: VARIABLE        TYPE        DESCRIPTION
            ---------------------------------------
            surface         Surface     pygame display to draw everything on
            x               int         x-coordinate of the menu
            y               int         y-coordinate of the menu
            shapes          list        contains all the Shape objects  
            buttons         list        contains all the CustomButton and Image Button objects
            images          list        contains all the Image objects 
            text            list        contains all the Text objects 
            open            bool        state of the menu opened/closed

draw -      Draws all the Shape, Button, Image, and Text objects
            NO PARAMETERS

'''
class Menu():

    def __init__(self, surface, x, y, shapes=[], buttons=[], images=[], texts=[], open=False):
        
        self.surface = surface
        self.x = x
        self.y = y

        self.shapes = shapes
        for shape in self.shapes:
            shape.offset(x,y)

        self.buttons = buttons
        for button in self.buttons:
            button.offset(x,y)
            if button is CustomButton:
                for shape in button.shapes:
                    shape.offset(x + button.rect.x, y + button.rect.y)
                for text in button.texts:
                    text.offset(x + button.rect.x, y + button.rect.y)
            elif button is ImageButton:
                button.image.offset(x,y)
        
        self.images = images
        for image in self.images:
            image.offset(x,y)

        self.texts = texts
        for text in self.texts:
            text.set_offset(x,y)
        self.open = open
    
    def draw(self):

        if self.open:

            for shape in self.shapes:
                shape.draw(self.surface)
            
            for button in self.buttons:
                button.draw(self.surface)
                
            for image in self.images:
                image.draw(self.surface)
            
            for text in self.texts:
                text.draw(self.surface)
    
    def toggle(self):
        self.open = not self.open
    
    def check_buttons(self, pos):
        for button in self.buttons:
            button.click(pos)

'''
CustomButton class - Used to define a button with Shape and Text objects

__init__ -  Declartion of a CustomButton 
Parameters: VARIABLE        TYPE        DESCRIPTION
            ---------------------------------------
            func            function    the function ran when the button is clicked
            args            any         arguments passed when func is ran
            shapes          list        contains all the Shape objects
            texts           list        contains all the Text objects
            x               int         x-coordinate of the button
            y               int         y-coordinate of the button

draw -      Draws all the Shape and Text objects
            NO PARAMETERS

offset -  Declartion of a CustomButton 
Parameters: VARIABLE        TYPE        DESCRIPTION
            ---------------------------------------
            x               int         if button is drawn on a menu, the x-offset of the menu
            y               int         if button is drawn on a menu, the y-offset of the menu

click -  Check if a coordinate is in a Rect 
Parameters: VARIABLE        TYPE        DESCRIPTION
            ---------------------------------------
            pos             tuple       the x and y of the position to be tested
'''
class CustomButton():

    def __init__(self, func, args=None, shapes=[], texts=[], x=0, y=0, width=0, height=0):
        
        self.rect = py.rect.Rect(x,y,width,height)
        self.shapes = shapes
        self.texts = texts
        self.func = func
        self.args = args
    
    def draw(self, surface):
        
        for shape in self.shapes:
            shape.draw()
        for text in self.texts:
            text.draw()
    
    def offset(self, x, y):
        self.rect.x += x
        self.rect.y += y
    
    def click(self, pos):
        if self.rect.collidepoint(pos):
            if self.args is None:
                self.func()
            else:
                self.func(self.args)

'''
ImageButton class - Used to define a button with a single Image object

__init__ -  Declartion of a ImageButton 
Parameters: VARIABLE        TYPE        DESCRIPTION
            ---------------------------------------
            func            function    the function ran when the button is clicked
            args            any         arguments passed when func is ran
            image           

draw -      Draws all the Shape and Text objects
            NO PARAMETERS

offset -  Declartion of a CustomButton 
Parameters: VARIABLE        TYPE        DESCRIPTION
            ---------------------------------------
            x               int         if button is drawn on a menu, the x-offset of the menu
            y               int         if button is drawn on a menu, the y-offset of the menu

click -  Check if a coordinate is in a Rect 
Parameters: VARIABLE        TYPE        DESCRIPTION
            ---------------------------------------
            pos             tuple       the x and y of the position to be tested
'''
class ImageButton():
    
    def __init__(self, func, args=None, image=None):
        
        self.image = image
        self.rect = self.image.rect
        self.func = func
        self.args = args
    
    def draw(self, surface):
        self.image.draw(surface)
        
    
    def offset(self, x, y):
        self.rect.x += x
        self.rect.y += y
    
    def click(self, pos):
        if self.rect.collidepoint(pos):
            if self.args is None:
                self.func()
            else:
                self.func(self.args)

class Shape():

    def __init__(self, fill, fill_color, border, border_color):
        self.fill = fill
        self.fill_color = fill_color
        self.border = border
        self.border_color = border_color

class Rect(Shape):

    def __init__(self, fill=False, fill_color=None, border=0, border_color=None, x=0, y=0, width=0, height=0):
        super().__init__(fill, fill_color, border, border_color)
        self.rect = py.rect.Rect(x, y, width, height)
    
    def draw(self, surface):
        if self.fill:
            py.draw.rect(surface, self.fill_color, self.rect)
        if self.border:
            py.draw.rect(surface, self.border_color, self.rect, self.border)
    
    def offset(self, x, y):
        self.rect.x += x
        self.rect.y += y

class Ellipse(Shape):

    def __init__(self, fill=False, fill_color=None, border=0, border_color=None, x=0, y=0, width=0, height=0):
        super().__init__(fill, fill_color, border, border_color)
        self.rect = py.rect.Rect(x,y,width,height)
    
    def draw(self, surface):
        if self.fill:
            py.draw.rect(surface, self.fill_color, self.rect)
        if self.border:
            py.draw.rect(surface, self.border_color, self.rect, self.border)
    
    def offset(self, x, y):
        self.rect.x += x
        self.rect.y += y

class Polygon(Shape):

    def __init__(self, fill=False, fill_color=None, border=0, border_color=None, points=[]):
        super().__init__(fill, fill_color, border, border_color)
        self.points = points

    def draw(self, surface):
        if self.fill:
            py.draw.polygon(surface, self.fill_color, self.points)
        if self.border:
            py.draw.rect(surface, self.border_color, self.points, self.border)

    def offset(self, x, y):
        for point in self.points:
            point[0] += x
            point[1] += y

class Image():
    
    def __init__(self, path, **kwargs):
        self.image = py.image.load(path)
        self.rect = self.image.get_rect(**kwargs)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def offset(self, x, y):
        self.rect.x += x
        self.rect.y += y

class Text():

    def __init__(self, font, size, text, color, **kwargs):
        self.offset_val = (0,0)
        self.kwargs = kwargs
        self.color = color
        self.font = py.font.SysFont(font, size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect(**kwargs)
    
    def draw(self, surface):
        surface.blit(self.text, self.rect)
    
    def offset(self):
        self.rect.x += self.offset_val[0]
        self.rect.y += self.offset_val[1]
    
    def set_offset(self, x, y):
        self.offset_val = (x,y)
        self.offset()
    
    def update_text(self, text):
        self.text = self.font.render(text, True, self.color)
        self.rect = self.text.get_rect(**self.kwargs)
        self.offset()