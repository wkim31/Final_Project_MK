#imports
import pygame
from pygame.locals import *
import time
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
border_mask = pygame.mask.from_surface(border)

mario_start = pygame.image.load('Mario-backside.png')
luigi = pygame.image.load('images/luigi-new.png')
#mario_start = scale_image(pygame.image.load("Mario-backside.png"), 0.05) 

# title
# pygame.display.set_caption("Race Karting Game!")
###
FPS = 60
path = [(50, 109), (120, 35), (214, 59), (286, 192), (357, 209), (431, 194), (478, 61), (558, 34), (652, 81), (681, 157), (668, 253), (627, 287), (271, 379), (258, 412), (293, 438), (628, 440), (672, 491), (677, 568), (634, 626), (534, 647), (438, 624), (416, 571), (330, 562), (243, 641), (168, 669), (81, 650), (44, 531), (49, 290)]

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.start_pos
        self.acceleration = 0.1

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

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self): #can move into PlayerCar class if u want
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y)) #we are subtracting the current car x and y positions from the positions of the other track border mask to give the displacement between the two masks; 
        poi = mask.overlap(car_mask, offset) #this returns the point of intersection between the two masks (the border mask and the car mask) if there is a collision/overlap
        return poi

class PlayerCar(AbstractCar):
    IMG = mario_start
    start_pos = (20, 305)

    def bounce(self):
     self.vel = -self.vel
     self.move()

class ComputerCar(AbstractCar):
    IMG = luigi
    start_pos = (-130,200)

    def __init__(self, max_vel, rotation_vel, path=[]):
        super().__init__(max_vel, rotation_vel)
        self.path = path
        self.current_point = 0
        self.vel = max_vel

    def draw_points(self, screen):
        for point in self.path:
            pygame.draw.circle(screen, (255, 0, 0), point, 5)

    def draw(self, screen): #when we draw the screen it will also draw all the points in the path for the computer car to follow
        super().draw(screen)
        #self.draw_points(screen)

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0: #to avoid having a division by 0
            desired_radian_angle = math.pi/2 #90 degrees
        else:
            desired_radian_angle = math.atan(x_diff/y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360 #turns in the oppo direction

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle))
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1

    def move(self): #ensures no index error if trying to move a point that doesn't exist
        if self.current_point >= len(self.path):
            return
        
        self.calculate_angle()
        self.update_path_point()
        super().move()

def draw(screen, player_car, computer_car):
    #  for img, pos in images:
    #      screen.blit(img, pos)
    
    player_car.draw(screen)
    computer_car.draw(screen)
    pygame.display.update()

# Run until the user asks to quit
running = True
clock = pygame.time.Clock()
# images = [bg_image, (0,0), border, (0,0)]
player_car = PlayerCar(100,2)
computer_car = ComputerCar(4,4,path)
while running:
    clock.tick(FPS) # while loop cannot run any faster than 60 frames per second
    draw(screen, player_car, computer_car)

   # updates the drawing window
    screen.blit(bg_image, (0, 0))
    screen.blit(border, (0,0))
    # finish line

    #pygame.display.update()

     # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #gives us the (x,y) coordinate of the mouse on the screen
            computer_car.path.append(pos) #adds that position to the computer car's path
    computer_car.move()  

     #change the angle by pressing a key
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_UP]:
        moved=True
        player_car.move_forward()
    if keys[pygame.K_DOWN]:
        moved=True
        player_car.move_backward()


    if not moved:
        player_car.reduce_speed()

    if player_car.collide(border_mask) != None:
        player_car.bounce()


print(computer_car.path)
# Done! Time to quit.
pygame.quit() 