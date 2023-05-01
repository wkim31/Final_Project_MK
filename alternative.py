#imports
import pygame
from pygame.locals import *
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
orange_car = scale_image(pygame.image.load("images/orange-car.png"), 0.05) 
#green_car = scale_image(pygame.image.load("green-car.png"), 0.169)

# title
pygame.display.set_caption("Race Karting Game!")
###
#FPS = 60

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 4
        self.rotation_vel = 5
        self.angle = 90
        self.x, self.y = self.start_pos
        self.acceleration = 0.5

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

    def move_right(self):
        self.x += self.vel
    
    def move_left(self):
        self.x -= self.vel
    
    def move_up(self):
        self.y -= self.vel
    
    def move_down(self):
        self.y += self.vel
    

class PlayerCar(AbstractCar):
    IMG = orange_car
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
player_car = PlayerCar(100,50)
# player_car2 = PlayerCar2(4,4)
clock = pygame.time.Clock()
while running:
   # clock.tick(FPS) # while loop cannot run any faster than 60 frames per second
    draw(screen, player_car)
    # draw(screen, player_car2)
   # updates the drawing window
    screen.blit(bg_image, (0, 0))
    screen.blit(border, (0,0))
   # screen.blit(orange_car,(0,0))
    # finish line

    #pygame.display.update()

     # Did the user click the window close button?
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        running = False
        break
     
     #change the angle by pressing a key
     keys = pygame.key.get_pressed()

     if keys[pygame.K_a]:
         player_car.rotate(left=True)
     if keys[pygame.K_d]:
         player_car.rotate(right=True)
     if keys[pygame.K_UP]:
         player_car.move_up()
     if keys[pygame.K_DOWN]:
         player_car.move_down()
     if keys[pygame.K_RIGHT]:
         player_car.move_right()
     if keys[pygame.K_LEFT]:
         player_car.move_left()
    

         

# Done! Time to quit.
pygame.quit() 