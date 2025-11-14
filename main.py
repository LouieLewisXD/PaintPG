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
BLACK = (0, 0, 0)

class Shape():
    
    def __init__(self,fill,drawn,border,border_color):
        self.fill = fill
        self.drawn = drawn
        self.border = border
        self.border_color = border_color

class Rect(Shape):
    
    def __init__(self,x,y,width,height,fill,drawn,border=0,border_color=0,origin=False):
        super().__init__(fill,drawn,border,border_color)
        if origin: self.origin = origin
        self.rect = py.rect.Rect(x,y,width,height)
    
    def draw(self):

        if self.fill != None:
            py.draw.rect(WIN,self.fill,self.rect)
        
        if self.border > 0:
            py.draw.rect(WIN, self.border_color, self.rect, self.border)
    
    def draw_preview(self, mouse_pos = None):
        if mouse_pos is None:
            mouse_pos = py.mouse.get_pos()
            if mouse_pos[0] > self.origin[0]:
                self.rect.x = self.origin[0]
                self.rect.width = mouse_pos[0] - self.rect.x
            else:
                self.rect.x = mouse_pos[0]
                self.rect.width = self.origin[0] - mouse_pos[0]

            if mouse_pos[1] > self.origin[1]:
                self.rect.y = self.origin[1]
                self.rect.height = mouse_pos[1] - self.rect.y
            else:
                self.rect.y = mouse_pos[1]
                self.rect.height = self.origin[1] - mouse_pos[1]

        else:
            self.origin = mouse_pos
            self.rect.topleft = mouse_pos
            self.rect.width = 5
            self.rect.height = 5




class Ellipse(Shape):

    def __init__(self,x,y,width,height,fill,drawn,border=0,border_color=0, origin=False):
        super().__init__(fill,drawn,border,border_color)
        if width == height: self.rect = py.rect.Rect(x - width / 2, y - height / 2, width, height)
        else: self.rect = self.rect = py.rect.Rect(x,y,width,height)
    
    def draw(self):
        if self.fill != None:
            py.draw.ellipse(WIN,self.fill,self.rect)
        
        if self.border > 0:
            py.draw.ellipse(WIN, self.border_color, self.rect, self.border)
    
    def draw_preview(self, mouse_pos = None):
        if mouse_pos is None:
            mouse_pos = py.mouse.get_pos()
            if mouse_pos[0] > self.origin[0]:
                self.rect.x = self.origin[0]
                self.rect.width = mouse_pos[0] - self.rect.x
            else:
                self.rect.x = mouse_pos[0]
                self.rect.width = self.origin[0] - mouse_pos[0]

            if mouse_pos[1] > self.origin[1]:
                self.rect.y = self.origin[1]
                self.rect.height = mouse_pos[1] - self.rect.y
            else:
                self.rect.y = mouse_pos[1]
                self.rect.height = self.origin[1] - mouse_pos[1]

        else:
            self.origin = mouse_pos
            self.rect.topleft = mouse_pos
            self.rect.width = 5
            self.rect.height = 5

class Circle(Shape):

    def __init__(self,pos,radius,fill,drawn=False,border=0,border_color=0):
        super().__init__(fill,drawn,border,border_color)
        self.pos = pos
        self.radius = radius
        self.rect = py.rect.Rect(pos[0] - radius, pos[1] - radius, radius * 2, radius * 2)
    
    def draw(self):
        if self.fill != None:
            py.draw.circle(WIN, self.fill, self.pos, self.radius)
        
        if self.border > 0:
            py.draw.circle(WIN, self.border_color, self.pos, self.border)
    
    def draw_preview(self, mouse_pos = None):
        if mouse_pos is None:
            mouse_pos = py.mouse.get_pos()
            self.radius = math.sqrt(math.pow(mouse_pos[0] - self.pos[0], 2) + math.pow(mouse_pos[1] - self.pos[1], 2))
            self.rect.width = self.radius * 2
            self.rect.height = self.radius * 2
            
        else:
            self.pos = mouse_pos
            self.rect.center = self.pos
        

class Poly(Shape):
    def __init__(self,points,fill,drawn=False,border=0,border_color=0):
        super().__init__(fill,drawn,border,border_color)
        self.points = points
    
    def draw(self):
        if len(self.points) > 2:
            if self.fill != None:
                py.draw.polygon(WIN, self.fill, self.points)
            
            if self.border > 0:
                py.draw.polygon(WIN, self.border_color, self.points, self.border)
        
        elif len(self.points) > 1:
            py.draw.line(WIN, self.fill, self.points[0], self.points[1])
        


    def draw_preview(self, mouse_pos = None):
        if mouse_pos is None:
            mouse_pos = py.mouse.get_pos()
            self.points[-1] = mouse_pos
        
        else:
            self.points.append(mouse_pos)
            self.points.append(mouse_pos)
        

class Line(Shape):
    def __init__(self,pos1,pos2,fill,border=1,drawn=False):
        super().__init__(fill,drawn,border,0)
        self.pos1 = pos1
        self.pos2 = pos2
        
    def draw(self):
        py.draw.line(WIN, self.fill, self.pos1, self.pos2, self.border)
    
    def draw_preview(self, mouse_pos=None):
        if mouse_pos is None:
            mouse_pos = py.mouse.get_pos()
            self.pos2 = mouse_pos
        
        else:
            self.pos1 = mouse_pos
            self.pos2 = mouse_pos

class Button():
    def __init__(self,x,y,path,func,arg):
        self.img = py.image.load(path)
        self.rect = self.img.get_rect(topleft = (x,y))
        self.func = func
        self.arg = arg
    
    def draw(self):
        WIN.blit(self.img, self.rect)
    
    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            waiting = True
            while waiting:
                for event in py.event.get():
                    if event.type == py.MOUSEBUTTONUP:
                        waiting = False
            self.func(self.arg)

shapes = []
preview_shape = None
preview = False
preview_drawing = False
buttons = []


draw = False
mouse_pos = ()
brush_size = 5

background = WHITE

#Brush size text
brush_size_label_text = sans_code.render("Brush Size", True, BLACK)
brush_size_label_rect = brush_size_label_text.get_rect(midleft = (5,415))

#Brush size number
brush_size_text = sans_code.render(str(brush_size), True, BLACK)
brush_size_rect = brush_size_text.get_rect(center = (55,460))

#Rect button

def tog_shape_preview(shape):
    global preview, preview_drawing, preview_shape, draw
    if preview:
        preview = False
        preview_drawing = False
        preview_shape = None
    else:
        preview = True
        match shape:
            case "rect":
                preview_shape = Rect(0,0,0,0,BLACK,False,0,0,True)
            case "ellipse":
                preview_shape = Ellipse(0,0,0,0,BLACK,False,0,0,True)
            case "circle":
                preview_shape = Circle((0,0),0,BLACK,False,0,0)
            case "line":
                preview_shape = Line((0,0),(0,0),BLACK)
            case "poly":
                preview_shape = Poly([],BLACK)
        





buttons.append(Button(150,410,"mario.jpg", tog_shape_preview, "rect"))
buttons.append(Button(300, 410, "mario.jpg", tog_shape_preview, "poly"))


def update():

    global draw, shapes, mouse_pos

    WIN.fill((background))

    if (py.mouse.get_pressed()[0] and not draw) and not preview:
        mouse_pos = py.mouse.get_pos()
        if mouse_pos[1] < 400:
            draw = True
            shapes.append(Circle(mouse_pos, brush_size / 2,BLACK))
    
    if draw and not preview:
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
    

    if preview:
        if preview_drawing: preview_shape.draw_preview()
        preview_shape.draw()
    
    
    py.draw.rect(WIN, WHITE, (0, 400, 750, 100))
    py.draw.line(WIN, BLACK, (0, 400), (750,400))
    WIN.blit(brush_size_label_text, brush_size_label_rect)
    WIN.blit(brush_size_text, brush_size_rect)

    for button in buttons:
        if py.mouse.get_pressed()[0]:
            button.check_click(py.mouse.get_pos())
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
                if preview and not preview_drawing:
                    preview_shape.draw_preview(mouse_pos)
                    preview_drawing = True
                elif preview and preview_drawing:
                    if type(preview_shape) is Poly:
                        if (not (preview_shape.points[-2] == mouse_pos)):
                            preview_shape.points.append(mouse_pos)
                            continue
                    preview_shape.origin = False
                    preview_shape.drawn = True
                    shapes.append(preview_shape)
                    preview = False
                    preview_drawing = False
                    preview_shape = None
        
        if event.type == py.KEYDOWN:
            if event.key == py.K_PERIOD and brush_size < 100:
                brush_size += 1
                brush_size_text = sans_code.render(str(brush_size), True, BLACK)
                brush_size_rect = brush_size_text.get_rect(center = (65,410))
            if event.key == py.K_COMMA and brush_size > 0:
                brush_size -= 1
                brush_size_text = sans_code.render(str(brush_size), True, BLACK)
                brush_size_rect = brush_size_text.get_rect(center = (65,410))
                
    
    update()
    py.display.update()
    clock.tick(30)