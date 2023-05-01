import pygame
def scale_image(img, factor):
    size = round(img.get_width()*factor),round(img.get_height()*factor)
    return pygame.transform.scale(img, size)

def blit_rotate_center(screen, image, top_left, angle):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft = top_left).center) #rotate around the center of the image; setting the center of the image as the top left corner bc pygame rotates rectangles from the top left corner
    


    print(rotated_image)
    print(new_rect.topleft)
    screen.blit(rotated_image, new_rect.topleft)