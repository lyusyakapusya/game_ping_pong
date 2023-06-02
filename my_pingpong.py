import pygame
from random import randint
pygame.init()


back = (200, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
mw.fill(back)

racket_x = 200
racket_y = 330

speed_x = 4
speed_y = 4

game_over = False
moving_right = False
moving_left = False

#end_flag
game_over = False

'''класс прямоугльник'''
 
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None): #его характериститки


'''класс мячик'''

class Picture(Area):
    def __init__(self, filename, x = 0, y = 0, width=10, height=10): #его характеристики


ball = Picture('ball.png', 160, 200, 50, 50) #мячик
platform_1 = Picture('platform.png',racket_x, racket_y, 100, 30) #платформа 1
platform_2 = Picture('platform.png',racket_x, racket_y, 100, 30) #платформа 2


start_x = 5
start_y = 5
count = 9
monsters = []



for i in range(3):
    y = start_x + (55 *i)
    x = start_y + (27.5 * i)

    for i in range(count):
        g = Picture('enemy.png', x, y, 50, 50)
        monsters.append(g)
        x = x+ 55

    count = count - 1

while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False



    if moving_left:
        platform.rect.x -=5

    if moving_right:
        platform.rect.x +=5

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1

    if ball.rect.colliderect(platform.rect):
        speed_y *= -1

    if ball.rect.y > 350 or monsters==[]:
        lose_game.fill()
        lose_game.draw()
        game_over = True

    for monster in monsters:
        monster.draw()
        if monster.rect.colliderect(ball.rect):
            monsters.remove(monster)
            monster.fill()
            speed_y *= -1

    platform.draw()
    ball.draw()




    pygame.display.update()
    clock.tick(40)
