import pygame as py

py.init()

# Menus can be opened, closed, have shapes, and buttons
class Menu():

    def __init__(self, surface, x, y, shapes=[], buttons=[], texts=[], open=False):
        
        self.surface = surface
        self.x = x
        self.y = y

        self.shapes = shapes
        for shape in self.shapes:
            shape.offset(x,y)

        self.buttons = buttons
        for button in self.buttons:
            button.offset(x,y)
            for shape in self.button.shapes:
                shape.offset(x + button.rect.x, y + button.rect.y)
            for text in self.button.texts:
                text.offset(x + button.rect.x, y + button.rect.y)

        self.texts = texts
        for text in self.texts:
            text.offset(x,y)
        self.open = open
    
    def draw(self):

        if open:

            for shape in self.shapes:
                shape.draw(self.surface)
            
            for button in self.buttons:
                button.draw(self.surface)
            
            for text in self.texts:
                text.draw(self.surface)

class Button():

    def __init__(self, func, args=None, shapes=[], texts=[], **kwargs):
        
        self.rect = py.rect.Rect(kwargs)
        self.shapes = shapes
        self.texts = texts
        self.func = func
        self.args = args
    
    def offset(self, x, y):
        self.rect.x += x
        self.rect.y += y
    
    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.func(self.args)

class Shape():

    def __init__(self, fill, fill_color, border, border_color):
        self.fill = fill
        self.fill_color = fill_color
        self.border = border
        self.border_color = border_color

class Rect(Shape):

    def __init__(self, fill=False, fill_color=None, border=0, border_color=None, **kwargs):
        super().__init__(fill, fill_color, border, border_color)
        self.rect = py.rect.Rect(kwargs)
    
    def draw(self, surface):
        if self.fill:
            py.draw.rect(surface, self.fill_color, self.rect)
        if self.border:
            py.draw.rect(surface, self.border_color, self.rect, self.border)
    
    def offset(self, x, y):
        self.rect.x += x
        self.rect.y += y

class Ellipse(Shape):

    def __init__(self, fill=False, fill_color=None, border=0, border_color=None, **kwargs):
        super().__init__(fill, fill_color, border, border_color)
        self.rect = py.rect.Rect(kwargs)
    
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

class Text():

    def __init__(self, font, size, text, color, **kwargs):
        self.offset_val = (0,0)
        self.kwargs = kwargs
        self.color = color
        self.font = py.font.SysFont(font, size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect(kwargs)
    
    def draw(self, surface):
        surface.blit(self.text, self.rect)
    
    def offset(self):
        self.rect.x += self.offset_val[0]
        self.rect.y += self.offset_val[1]
    
    def update_text(self, text):
        self.text = self.font.render(text, True, self.color)
        self.rect = self.text.get_rect(self.kwargs)
        self.offset()