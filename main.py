import pygame as py
import sys

py.init()
run = True

WIDTH, HEIGHT = 1080,720

WIN = py.display.set_mode((WIDTH, HEIGHT))

clock = py.time.Clock()

sans_code = py.font.Font("SansCode.ttf", 20)

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
        if width == height: self.rect = py.rect.Rect(x - width / 2, y - height / 2, width, height)
        else: self.rect = self.rect = py.rect.Rect(x,y,width,height)
    
    def draw(self):
        if self.fill != None:
            py.draw.elipse(WIN,self.fill,self.rect)
        
        if self.border > 0:
            py.draw.elipse(WIN, self.border_color, self.rect, self.border)

class Circle(Shape):

    def __init__(self,pos,radius,fill,border=0,border_color=0):
        super().__init__(fill,border,border_color)
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.radius = radius
        self.rect = py.rect.Rect(self.x - radius, self.y - radius, radius * 2, radius * 2)
    
    def draw(self):
        if self.fill != None:
            py.draw.circle(WIN, self.fill, self.pos, self.radius)
        
        if self.border > 0:
            py.draw.circle(WIN, self.border_color, self.pos, self.border)

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
    def __init__(self,pos1,pos2,fill,border=1):
        super().__init__(fill,border,0)
        self.pos1 = pos1
        self.pos2 = pos2
        
    def draw(self):
        py.draw.line(WIN, self.fill, self.pos1, self.pos2, self.border)

class Button():
    def __init__(self,x,y,path,func):
        self.img = py.image.load(path)
        self.rect = self.img.get_rect(topleft = (x,y))
        self.func = func
    
    def draw(self):
        WIN.blit(self.img, self.rect)
    
    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.func

shapes = []
preview_shape = None
buttons = []


draw = False
mouse_pos = ()
brush_size = 5

background = WHITE

#Brush size text
brush_size_label_text = sans_code.render("Brush Size", True, BLACK)
brush_size_label_rect = brush_size_label_text.get_rect(midleft = (5,660))

#Brush size number
brush_size_text = sans_code.render(str(brush_size), True, BLACK)
brush_size_rect = brush_size_text.get_rect(center = (65,690))

#Rect button

def draw_rect_preview():
    print("hi")

buttons.append(Button(200,645,"mario.jpg", draw_rect_preview))



def update():

    global draw, shapes, mouse_pos

    WIN.fill((background))

    if py.mouse.get_pressed()[0] and not draw:
        mouse_pos = py.mouse.get_pos()
        if mouse_pos[1] < 640:
            draw = True
            shapes.append(Circle(mouse_pos, brush_size / 2,BLACK))
    
    if draw:
        cur_mouse_pos = py.mouse.get_pos()
        shapes.append(Line(mouse_pos, cur_mouse_pos, BLACK, brush_size))
        shapes.append(Circle(cur_mouse_pos, brush_size / 2,BLACK))
        mouse_pos = cur_mouse_pos
        if not py.mouse.get_pressed()[0]:
            shapes.append(Line(mouse_pos, py.mouse.get_pos(), BLACK, brush_size))
            shapes.append(Circle(py.mouse.get_pos(), brush_size / 2,BLACK))
            draw = False

    for shape in shapes:
        shape.draw()
    
    py.draw.rect(WIN, WHITE, (0, 640, 1080, 80))
    py.draw.line(WIN, BLACK, (0, 640), (1080,640))
    WIN.blit(brush_size_label_text, brush_size_label_rect)
    WIN.blit(brush_size_text, brush_size_rect)

    for button in buttons:
        button.check_click(py.mouse.get_pos)
        button.draw()


while run:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
            py.quit()
            sys.exit()
        
        if event.type == py.MOUSEBUTTONDOWN:
            if py.mouse.get_pressed()[0]:

                mouse_pos = py.mouse.get_pos()
                for button in buttons:
                    button.check_click(mouse_pos)
        
        if event.type == py.KEYDOWN:
            if event.key == py.K_PERIOD and brush_size < 100:
                brush_size += 1
                brush_size_text = sans_code.render(str(brush_size), True, BLACK)
                brush_size_rect = brush_size_text.get_rect(center = (65,690))
            if event.key == py.K_COMMA and brush_size > 0:
                brush_size -= 1
                brush_size_text = sans_code.render(str(brush_size), True, BLACK)
                brush_size_rect = brush_size_text.get_rect(center = (65,690))
                
    
    update()
    py.display.update()
    clock.tick(30)