#imports:
import pygame
from pygame.locals import *
import time
import random

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
# track border
# finish line
orange_car = pygame.image.load("images/orange-car.png") 
green_car = pygame.image.load("images/green-car.png")

#clock:
clock = pygame.time.Clock()
#colors:
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
cadet_blue = (142, 229, 238)
cyan = (0, 238, 238)
# title
def car(x, y):
    screen.blit(mario_start, (x, y))

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

def crash():
    message_display('You Crashed')

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


def game_loop():
    FPS = 60
    #variables for car:
    x = (WIDTH * 0.5)
    y = (HEIGHT * 0.5)
    y_change = 0
    x_change = 0
    car_speed = 0

    # Run until the user asks to quit
    running = True
    clock = pygame.time.Clock()
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    y_change = 0
                    x_change = 0
        y += y_change
        x += x_change

        screen.blit(bg_image, (0, 0))
        car(x, y)

        pygame.display.update()
        clock.tick(FPS) 
    # Done! Time to quit.
game_intro()

game_loop()
pygame.quit() 
quit()