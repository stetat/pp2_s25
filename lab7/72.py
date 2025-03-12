import pygame
import os
import time

pygame.mixer.pre_init(44100, -16, 2, 512) 
pygame.init()

storage = ["resources/try1.ogg", "resources/try2.ogg", "resources/try3.ogg"]
cur = 0

def play_music(cur):
    global storage
    pygame.mixer.music.stop()
    time.sleep(1)
    pygame.mixer.music.load(storage[cur])
    pygame.mixer.music.play(-1)
    

_img_lib = {}
def get_image(path):
    global _img_lib
    image = _img_lib.get(path)
    if image == None:
        cand_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(cand_path)
        _img_lib[path] = image
    return image

screen = pygame.display.set_mode((840, 750))
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        play_music(cur)
    
    elif pressed[pygame.K_RIGHT]:
        cur = (cur+1)%3
        play_music(cur)

    elif pressed[pygame.K_LEFT]:
        cur = (cur-1)%3
        play_music(cur)
    
    elif pressed[pygame.K_SPACE]:
        pygame.mixer.music.stop()

    screen.fill((255,255,255))



    screen.blit(get_image("resources/cntrls.png"), (0, 0))
    pygame.display.flip()
    clock.tick(60)

    
