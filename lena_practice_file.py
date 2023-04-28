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

# title
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
        pygame.display.update()
        clock.tick(15)

def game_loop():
    FPS = 60

    # Run until the user asks to quit
    running = True
    clock = pygame.time.Clock()
    while running:
    # updates the drawing window
        screen.blit(bg_image, (0, 0))
        # finish line
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
        clock.tick(FPS) 
        
    # Done! Time to quit.
game_intro()
game_loop()
pygame.quit() 