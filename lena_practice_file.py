#imports:
import pygame
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
pause = False

class Gadget:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y
    def display(self):
        screen.blit(self.img, (self.x, self.y))

# class Char:
#     def __init__(self, img, x, y):
#         self.img = img
#         self.x = x
#         self.y = y
#     def display(self):
#         screen.blit(self.img, (self.x, self.y))

banana_list = [Gadget(banana,  80, 100), Gadget(banana, 900, 100), Gadget(banana, 60, 750)]
star_list = [Gadget(star, 930, 300), Gadget(star, 500, 800)]

#mario = Char(mario_start, 80, 400)

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
    print(click)
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
            print(event)
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
    angle = 0
    bg = screen
    img1 = mario_start
    x_change = 0
    y_change = 0
    angle_change = 0
    SPEED = 2
    gad = banana_list
    global pause

    # Run until the user asks to quit
    running = True
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
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


        if x > 1000:
            x = 1000
        elif x < 0:
            x = 0
        else: 
            x+= x_change
        if y > 1000:
            y = 1000
        elif y < 0:
            y = 0
        else:
            y += y_change
        #x += x_change
        angle += angle_change

        screen.blit(bg_image, (0, 0))
        car(bg, img1, x, y, angle)
        for item in banana_list:
                item.display()
        for item in star_list:
            item.display()
        
        #player_car

        pygame.display.update()
        clock.tick(FPS) 
    # Done! Time to quit.
game_intro()

game_loop()
pygame.quit() 
quit()