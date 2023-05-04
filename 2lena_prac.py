#imports:
import pygame
from abstract_Car_code import *
from pygame.locals import *
import time
import random
from utils import blit_rotate_center
from dataclasses import dataclass

pygame.init()
pygame.font.init()
#Define game state:
# Set up the drawing window
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Race Karting Game!")
bg_image = pygame.image.load('images/fin_track-mariocircuit-3.png')
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
mario_start = pygame.image.load('Mario-backside.png')
luigi = pygame.image.load('images/luigi-2 (1).png')
banana = pygame.image.load('images/banana.png')
star = pygame.image.load('images/star.png')
# track border
# finish line
orange_car = pygame.image.load("images/orange-car.png") 

#clock:
clock = pygame.time.Clock()
#colors:
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
cadet_blue = (142, 229, 238)
cyan = (0, 238, 238)
green = (69, 139, 0)
bright_green = (127, 255, 0)
orange = (255, 153, 18)
bright_orange = (255, 97, 3)
# title
#Globals:
pause = False
out = False
angle_change = 0
spin = False
class Gadget:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y  
    def display(self):
        screen.blit(self.img, (self.x, self.y))

#mario = Char(mario_start, 80, 400)
# class ComputerCar(AbstractCar): 
#     IMG = luigi
#     START_POS = (35, 305)

#     def __init__(self, max_vel , rotation_vel, path=[]):
#         super().__init__(max, rotation_vel)
#         self.path = path
#         self.current_point = 0 
#         self.vel = max_vel
#     def draw_points(self, win):
#         for point in self.path:
#             pygame.draw.circle(win, (255, 0, 0), point, 5)
    
#     def draw(self, win):
#         super().draw(win)
#         #self.draw_points(win)
    


# def draw(win, images, player_car, computer_car):
#     for img, pos in images:
#         win.blit(img, pos)
#     player_car.draw(win)
#     computer_car.draw(win)
#     pygame.display.update()


def car(bg, img1, x, y, angle):
    blit_rotate_center(bg, img1, (x, y), angle)

def text_objects(txt, font):
    '''Object for text class given inputted string and font'''
    txtsurface = font.render(txt, True, red)
    return txtsurface, txtsurface.get_rect()

def message_display(txt):
    '''displays message according to fonts using text_objects'''
    largeText = pygame.font.SysFont('georgia', 80)
    txtsurf, txtrect =  text_objects(txt, largeText)
    txtrect.center = ((WIDTH/2), (HEIGHT/3.5))
    screen.blit(txtsurf, txtrect)

    pygame.display.update()
    time.sleep(2)
    game_loop()



def button(msg, x, y, w, h, ic, ac, action = None):
    '''button-pressed function. message, x coord, y coord, width, heigh, initial color, 
    action color'''
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smallText = pygame.font.SysFont('georgia', 20)
    textsurf, textrect = text_objects(msg, smallText)
    textrect.center = ( (x + (w/2)), (y + (h/2) ))
    screen.blit(textsurf, textrect)

def game_intro():
    '''start screen'''
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(black)
        largeText = pygame.font.SysFont('georgia', 80)
        txtsurf, txtrect = text_objects('2D Mario Kart!', largeText)
        txtrect.center = ((WIDTH/2), (HEIGHT/3.5))
        screen.blit(txtsurf, txtrect)
        

        button("Go!", 450, 450, 100, 50, cadet_blue, cyan, game_loop)
        pygame.display.update()
        clock.tick(15)

def quitgame():
    '''helper for pause'''
    pygame.quit()
    quit()

def finish_line():
    '''finish line screen. Choice: go on to next level, or quit game'''
    #out = True

    while out:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(black)
        largeText = pygame.font.SysFont('georgia', 80)
        txtsurf, txtrect = text_objects('finished!', largeText)
        txtrect.center = ((WIDTH/2), (HEIGHT/3.5))
        screen.blit(txtsurf, txtrect)
        button("Next Level", 150, 450, 100, 50, cadet_blue, cyan, game_loop)
        button("Quit", 700, 450, 100, 50, cadet_blue, cyan, quitgame)

        pygame.display.update()
        clock.tick(15)

def unpause():
    '''helper for pause'''
    global pause
    pause = False

def paused():

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(black)
        largeTxt = pygame.font.SysFont('georgia', 100)
        ts, tr = text_objects("Paused", largeTxt)
        tr.center = ((WIDTH/2), (HEIGHT/4))
        screen.blit(ts, tr)
        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 700, 450, 100, 50, orange, bright_orange, quitgame)
        pygame.display.update()
        clock.tick(15)


def game_loop():
    FPS = 60
    #variables for car:
    x = (80)
    y = (400)
    x2 = (35)
    y2 = (305)
    angle = 0
    bg = screen
    img1 = mario_start
    img2 = luigi
    x_change = 0
    y_change = 0
    x2_change = 3
    y2_change = 3
    banana_list = [Gadget(banana,  80, 100), Gadget(banana, 900, 100), Gadget(banana, 60, 750)]
    star_list = [Gadget(star, 930, 300), Gadget(star, 500, 800), Gadget(star, 200, 850)]
    global angle_change
    SPEED = 5
    banana_speed = 2
    star_speed = 7
    global pause
    global out
    

    # Run until the user asks to quit
    running = True
    clock = pygame.time.Clock()
    #keys = pygame.key.get_pressed()
    time_now = 0
    computer_car = ComputerCar(4, 4)
    while running:
        draw(WIN, images, player_car, computer_car)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                for item in banana_list:
                    if ((item.x + 32) >= x >= (item.x)) and ((item.y + 32) >= y >= (item.y)) or ((item.x + 32) >= x + 32 >= (item.x)) and ((item.y + 32) >= y + 32 >= (item.y)):
                        time_now = pygame.time.get_ticks()
                        SPEED = banana_speed
                        banana_list.remove(item)
                if pygame.time.get_ticks() >= time_now + 3000:
                    SPEED = 5
                    print("this is the speed,", SPEED)

                for item in star_list:
                    if ((item.x + 32) >= x >= (item.x)) and ((item.y + 32) >= y >= (item.y)) or ((item.x + 32) >= x + 32 >= (item.x)) and ((item.y + 32) >= y + 32 >= (item.y)):
                        time_now = pygame.time.get_ticks()
                        SPEED = star_speed
                        star_list.remove(item)
                if pygame.time.get_ticks() >= time_now + 3000:
                    SPEED = 5

                if event.key == pygame.K_UP:
                    y_change = -SPEED
                if event.key == pygame.K_DOWN:
                    y_change = SPEED
                if event.key == pygame.K_LEFT:
                    x_change = -SPEED
                if event.key == pygame.K_RIGHT:
                    x_change = SPEED
                if event.key == pygame.K_a:
                    angle_change = 2
                if event.key == pygame.K_d:
                   angle_change = -2
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                all = event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_p
                if all:
                    y_change = 0
                    x_change = 0
                    angle_change = 0

        #boundaries:
        if x > WIDTH - 5:
            x = 995
        elif x < 0:
            x = 0
        else: 
            x+= x_change

        if y > HEIGHT:
            y = HEIGHT
        elif y < 0:
            y = 0
        else:
            y += y_change

        angle += angle_change

        ######)
        if (405 < y < 412) and (85 > x > 20):
            #diff of 7 acounts for max speed.
            out = True
            finish_line()
        ######
        screen.blit(bg_image, (0, 0))
        #luigi:
        car(bg, img2, x2, y2, angle)

        #mario:
        car(bg, img1, x, y, angle)
        for item in banana_list:
            item.display()
        for item in star_list:
            item.display()
        

        pygame.display.update()
        clock.tick(FPS) 
    # Done! Time to quit.

game_intro()

game_loop()
pygame.quit() 
quit()