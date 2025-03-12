import pygame


pygame.init()
screen = pygame.display.set_mode((490, 490))
done = False
clock = pygame.time.Clock()

x = 25
y = 25

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN] and y+45 <= 490: y+=20
    elif pressed[pygame.K_UP] and y-35 >= 0: y-=20
    elif pressed[pygame.K_RIGHT] and x+45 <= 490: x+=20
    elif pressed[pygame.K_LEFT] and x-35 >= 0: x-=20

    screen.fill((255, 255, 255))

  

    pygame.draw.circle(screen, (220, 0, 0), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)
    