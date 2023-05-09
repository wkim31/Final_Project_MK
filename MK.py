#imports
import pygame
from pygame.locals import *
import math
import time
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

FINISH = pygame.image.load('images/track-finish.png')
FINISH = pygame.transform.scale(FINISH, (WIDTH, HEIGHT))
FINISH_MASK = pygame.mask.from_surface(FINISH)

mario_start = pygame.image.load('newMario-backside.png')
luigi = pygame.image.load('images/LUIGI.png')
mario_start = scale_image(pygame.image.load("newMario-backside.png"), 1.1) 
luigi = scale_image(pygame.image.load("images/LUIGI.png"), 0.7)

title_screen = pygame.image.load('images/game icon.gif')
title_screen = pygame.transform.scale(title_screen, (WIDTH, HEIGHT))
pause_screen = pygame.image.load('images/Mario Kart instructions.png')

finish = pygame.image.load('images/celebrate.jpeg')
finish = pygame.transform.scale(finish, (WIDTH, HEIGHT))
FINISH_POSITION = (3, 3)

banana = pygame.image.load('images/banana.png')
banana_mask = pygame.mask.from_surface(banana)
star = pygame.image.load('images/star.png')
star_mask = pygame.mask.from_surface(star)
ghost = pygame.image.load('images/ghost.png')
ghost_mask = pygame.mask.from_surface(ghost)

# colors:
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
dark_blue = (0, 0, 205)
cadet_blue = (142, 229, 238)
cyan = (0, 238, 238)
green = (69, 139, 0)
bright_green = (127, 255, 0)
orange = (255, 153, 18)
bright_orange = (255, 97, 3)

#globals: 
pause = False
out = False
clock = pygame.time.Clock() 

#screens (start menus, end menus, pause menus)
def text_objects(txt, font):
    '''Object for text class given inputted string and font'''
    txtsurface = font.render(txt, True, white)
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
        screen.blit(title_screen, (0, 0))
        button("Go!", 300, 300, 130, 60, dark_blue, cyan, game_loop)
        pygame.display.update()
        clock.tick(15)

def quitgame():
    '''helper for pause'''
    pygame.quit()
    quit()

def finish_line_1():
    '''finish line screen. Choice: go on to next level, or quit game'''
    out = True

    while out:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(finish, (0, 0))
        button("1st Place!", 300, 170, 100, 50, bright_green, bright_green, None)
        button("Next Level", 200, 570, 100, 50, cadet_blue, cyan, game_loop_2)
        button("Quit", 400, 570, 100, 50, cadet_blue, cyan, quitgame)

        pygame.display.update()
        clock.tick(15)

def com_victory():
    out = True
    while out:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(black)
        largeText = pygame.font.SysFont('georgia', 80)
        txtsurf, txtrect = text_objects('You lose :(', largeText)
        txtrect.center = ((WIDTH/2), (HEIGHT/3.5))
        screen.blit(txtsurf, txtrect)
        

        button("Try Again", 450, 450, 100, 50, cadet_blue, cyan, game_loop)
        button("Quit Now", 150, 450, 100, 50, cadet_blue, cyan, quitgame)
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
        screen.fill(white)
        screen.blit(pause_screen, (0, 0))
        button("Continue", 200, 630, 100, 50, green, bright_green, unpause)
        button("Quit", 400, 630, 100, 50, orange, bright_orange, quitgame)
        pygame.display.update()
        clock.tick(15)
# title#
###
FPS = 60
path = [(52, 87), (131, 35), (214, 66), (291, 201), (435, 199), (491, 58), (605, 43), (677, 136), (662, 260), (256, 373), (295, 425), (610, 424), (682, 478), (657, 583), (533, 642), (440, 614), (436, 559), (339, 556), (224, 646), (81, 628), (49, 290)]

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

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y)) #we are subtracting the current car x and y positions from the positions of the other track border mask to give the displacement between the two masks; 
        poi = mask.overlap(car_mask, offset) #this returns the point of intersection between the two masks (the border mask and the car mask) if there is a collision/overlap
        return poi

class PlayerCar(AbstractCar):
    IMG = mario_start
    start_pos = (20, 255)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
     self.vel = -self.vel
     self.move()

class ComputerCar(AbstractCar):
    IMG = luigi
    start_pos = (50,250)

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
       # self.draw_points(screen)

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

def draw(screen, images, img_banana, player_car, computer_car):
    for img, pos in images:
        screen.blit(img, pos)
    for img, pos in img_banana:
        screen.blit(img, pos)

    player_car.draw(screen)
    computer_car.draw(screen)
    #pygame.display.update()

def handle_collision(player_car, computer_car, img_banana):
    computer_finish_poi_collide = computer_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if computer_finish_poi_collide != None:
       com_victory()

    player_finish_poi_collide = player_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 284:
            #if the y coordinate is 284, and poi is not none, this means the player tried to cross the finish line backwards
            player_car.bounce()
        else:
            finish_line_1()
    for item, pos in img_banana:
        banana_finish_poi_collide = player_car.collide(banana_mask, *pos)
        if banana_finish_poi_collide != None:
            player_car.bounce()
            img_banana.remove((item, pos))


def game_loop():
    running = True
    images = [(FINISH, FINISH_POSITION)]
    img_banana = [(banana, (133, 49)), (banana, (400, 200)), (banana, (635, 460)), (banana, (50, 500))]
    #img_star = [(star, (460, 300)), (star, (355, 550)), (star, (215, 370))]
    player_car = PlayerCar(4, 4)
    computer_car = ComputerCar(2,6,path)
    # clock = pygame.time.Clock()
    global out
    global pause
    while running:
        clock.tick(FPS) # while loop cannot run any faster than 60 frames per second
        draw(screen, images, img_banana, player_car, computer_car)

    # updates the drawing window
        screen.blit(bg_image, (0, 0))
        screen.blit(border, (0,0))
        # finish line

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break        

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pos = pygame.mouse.get_pos() #gives us the (x,y) coordinate of the mouse on the screen
            #     computer_car.path.append(pos) #adds that position to the computer car's path
        
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
        if keys[pygame.K_p]:
            pause = True
            paused()


        if not moved:
            player_car.reduce_speed()

        if player_car.collide(border_mask) != None:
            player_car.bounce()
        
        handle_collision(player_car, computer_car, img_banana)
        draw(screen, images, img_banana, player_car, computer_car)

        pygame.display.update()

    print(computer_car.path)

##Next level:
def draw_2(screen, images, img_banana, img_star, img_ghost, player_car, computer_car):
    for img, pos in images:
        screen.blit(img, pos)
    for img, pos in img_banana:
        screen.blit(img, pos)
    for img, pos in img_star:
        screen.blit(img, pos)
    for img, pos in img_ghost:
        screen.blit(img, pos)

    player_car.draw(screen)
    computer_car.draw(screen)

def handle_collision_2(player_car, computer_car, img_banana, img_star, img_ghost):
     computer_finish_poi_collide = computer_car.collide(
        FINISH_MASK, *FINISH_POSITION)
     if computer_finish_poi_collide != None:
       com_victory()

     player_finish_poi_collide = player_car.collide(
        FINISH_MASK, *FINISH_POSITION)
     if player_finish_poi_collide != None:
        #print("THIS IS!!!!!!!!!!!!!" + str(player_finish_poi_collide))
        if player_finish_poi_collide[1] == 284:
            #if the y coordinate is 284, and poi is not none, this means the player tried to cross the finish line backwards
            player_car.bounce()
        else:
            finish_line_1()
     for item, pos in img_banana:
        banana_finish_poi_collide = player_car.collide(banana_mask, *pos)
        if banana_finish_poi_collide != None:
            img_banana.remove((item, pos))
            player_car.bounce()          
     for (item, pos) in img_star:
        star_finish_poi_collide = player_car.collide(star_mask, *pos)
        if star_finish_poi_collide != None:
            img_star.remove((item, pos))
            #player_car.
     for (item, pos) in img_ghost:
        ghost_poi_collide = player_car.collide(ghost_mask, *pos)
        if ghost_poi_collide != None:
            img_ghost.remove((item, pos))
            player_car.reduce_speed()



def game_loop_2():
    #level 2
    running = True
    images = [(FINISH, FINISH_POSITION)]
    img_banana = [(banana, (133, 49)), (banana, (400, 200)), (banana, (635, 460)), (banana, (50, 500))]
    img_star = [(star, (460, 300)), (star, (355, 550)), (star, (215, 370))]
    img_ghost = [(ghost, (50, 600)), (ghost, (418, 418)), (ghost, (350, 200))]
    player_car = PlayerCar(100, 1)
    computer_car = ComputerCar(4,4,path)
    clock = pygame.time.Clock()
    global out
    global pause
    while running:
    # clock.tick(FPS) # while loop cannot run any faster than 60 frames per second
        #draw(screen, images, img_banana, img_star, player_car, computer_car)

    # updates the drawing window
        screen.blit(bg_image, (0, 0))
        screen.blit(border, (0,0))
        # finish line

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break        

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() #gives us the (x,y) coordinate of the mouse on the screen
                computer_car.path.append(pos) #adds that position to the computer car's path
        
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
        if keys[pygame.K_p]:
            pause = True
            paused()


        if not moved:
            player_car.reduce_speed()

        if player_car.collide(border_mask) != None:
            player_car.bounce()
        
        handle_collision_2(player_car, computer_car, img_banana, img_star, img_ghost)
        draw_2(screen, images, img_banana, img_star, img_ghost, player_car, computer_car)

        pygame.display.update()


game_intro()
game_loop()
# Done! Time to quit.
pygame.quit() 
quit()