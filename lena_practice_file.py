#imports:
import pygame
from pygame.locals import *

#Define game state:
# Set up the drawing window
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bg_image = pygame.image.load('images/fin_track-mariocircuit-3.png')
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
# track border
# finish line
orange_car = pygame.image.load("images/orange-car.png") 
green_car = pygame.image.load("images/green-car.png")

#Classes:
#class Player(pygame.sprite.Sprite): 




#Initialize game:
pygame.init()


# title
pygame.display.set_caption("Race Karting Game!")

FPS = 60

# Run until the user asks to quit
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS) # while loop cannot run any faster than 60 frames per second
   
   # updates the drawing window
    screen.blit(bg_image, (0, 0))
    # finish line

    pygame.display.update()

     # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

# Done! Time to quit.
pygame.quit() 