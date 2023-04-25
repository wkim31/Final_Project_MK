#imports:
import pygame
from pygame.locals import *
pygame.init()

# Set up the drawing window
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bg_image = pygame.image.load('fin_bg-mario-circuit-3.png')
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

# Done! Time to quit.
pygame.quit() 