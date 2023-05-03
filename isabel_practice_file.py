#imports
import pygame
from pygame.locals import *
import math
pygame.init()
from utils import scale_image, blit_rotate_center

# Set up the drawing window
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg_image = pygame.image.load("images/fin_track-mariocircuit-3.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
border = pygame.image.load("images/fin_trackborder-mariocircuit-3.png")
border = pygame.transform.scale(border, (WIDTH, HEIGHT))
# finish line
mario_start = pygame.image.load('Mario-backside.png')
#mario_start = scale_image(pygame.image.load("Mario-backside.png"), 0.05) 
#green_car = scale_image(pygame.image.load("green-car.png"), 0.169)

# title
pygame.display.set_caption("Race Karting Game!")
###
#FPS = 60

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.start_pos
        self.acceleration = 0.025

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, screen):
        blit_rotate_center(screen, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians)* self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()


class PlayerCar(AbstractCar):
    IMG = mario_start
    start_pos = (10, 305)

def draw(screen, player_car):
#     for img, pos in images:
#         screen.blit(img, pos)
    
    player_car.draw(screen)
    pygame.display.update()

# class PlayerCar2(AbstractCar):
#     IMG = green_car
#     start_pos = (25, 305)

# def draw(screen, player_car2):
#     for img, pos in images:
#         screen.blit(img, pos)
    
    # player_car2.draw(screen)
    # pygame.display.update()

# Run until the user asks to quit
running = True
images = [bg_image, (0,0)]
player_car = PlayerCar(100,2)
clock = pygame.time.Clock()
while running:
   # clock.tick(FPS) # while loop cannot run any faster than 60 frames per second
    draw(screen, player_car)

   # updates the drawing window
    screen.blit(bg_image, (0, 0))
    screen.blit(border, (0,0))
    # screen.blit(mario_start,(0,0))
    # finish line

    #pygame.display.update()

     # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
     
     #change the angle by pressing a key
    keys = pygame.key.get_pressed()
    move = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_UP]:
        move=True
        player_car.move_forward()
    # if keys[pygame.K_RIGHT]:
    #     player_car.move_right()
    # if keys[pygame.K_LEFT]:
    #     player_car.move_left()

    if not move:
        player_car.reduce_speed()

         
# Done! Time to quit.
pygame.quit() 