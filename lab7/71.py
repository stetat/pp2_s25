import pygame
import os
import time

_img_lib = {}
def get_image(path):
    global _img_lib
    image = _img_lib.get(path)
    if image is None:
        cand_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(cand_path)
        _img_lib[path] = image
    return image



pygame.init()
screen = pygame.display.set_mode((1000, 1000))
done = False
clock = pygame.time.Clock()

minutes = pygame.image.load("resources/mins.png")
seconds = pygame.image.load("resources/sz.png")
scaled_sec = pygame.transform.scale(seconds, (seconds.get_width()*1.4, seconds.get_height()*1.4))
scaled_min = pygame.transform.scale(minutes, (minutes.get_width()*1.4, minutes.get_height()*1.4))
casy = pygame.image.load("resources/clock.png").convert()
ysac = pygame.transform.scale(seconds, (200, 200))

pivot = (539, 508)
pivot1 = (450, 508)
angle = 0
angle1 = 0








def rotate_around_pivot(image, angle, pivot):
    """ Rotates an image around a pivot point and returns the new image and rect """
 

    # Rotate the image
    rotated_image = pygame.transform.rotate(image, -angle)  # Negative for clockwise

    # Get the new bounding rect and set its center to pivot
    rotated_rect = rotated_image.get_rect()

    rotated_rect.center = pivot

    return rotated_image, rotated_rect

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    angle += 0.1
    angle1 += 1/600

    rotated_sec, rotated_sec_rect = rotate_around_pivot(scaled_sec, angle, pivot)
    rotated_min, rotated_min_rect = rotate_around_pivot(scaled_min, angle1, pivot1)
    

    screen.fill((255, 255, 255))
    screen.blit(casy, (-200, 0))
    screen.blit(rotated_sec, rotated_sec_rect.topleft)
    screen.blit(rotated_min, rotated_min_rect.topleft)

    

    pygame.display.flip()
    clock.tick(60)
