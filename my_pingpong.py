from pygame import *
from random import randint


clock = time.Clock()
back = (200, 255, 255) #цвет фона (background)
mw = display.set_mode((500, 500)) #окно программы (main window)
mw.fill(back)
clock = time.Clock()
game_over = False


'''класс прямоугльник'''
 
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None): #его характериститки
        self.rect = Rect(x, y, width, height) #прямоугольник
        self.fill_color = back
        if color:
            self.fill_color = color
    def update(self):
        keys_passed = key.get_pressed()
        if keys_passed[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_passed[K_DOWN] and self.rect.x < win_width -80:
            self.rect.x += self.speed

 
    def color(self, new_color):
        self.fill_color = new_color
 
 
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        
    def collidepoint(self,x, y):
        return self.rect.collidepoint(x, y)

    def collidepoint(self, rect):
        return self.rect.collidepoint(rect)


'''класс мячик'''

class Picture(Area):
    def __init__(self, filename, x = 0, y = 0, width=10, height=10):
        Area.__init__(self, x = x, y=y, width=width, height=height, color = None)
        self.image = image.load(filename) 

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
#его характеристики


ball = Picture('ball.png', 160, 200, 50, 50) #мячик
platform_1 = Picture('platform.png', 0, 0, 100, 30) #платформа 1
platform_2 = Picture('platform.png',0, 0, 100, 20) #платформа 2


while not game_over:
    for e in event.get():
        if e.type == QUTI:
            game = False
    ball.fill()
    platform_1.fill()
    platform_2.fill()


''' вырисовываем мачик и платформы'''
platform_1.draw()
platform_2.draw()
ball.draw()
pygame.display.update()
