import pygame
import time
import random
from game_object import GameObject
from worm import Worm
from food import Food
from wall import Wall

#Set up the background tiles
def create_background(screen, width, height):
    colors = [(255, 255, 255), (212, 212, 212)]
    tile_width = 20
    for y in range(0, height, tile_width):
        for x in range(0, width, tile_width):
            row = y // tile_width
            col = x // tile_width
            pygame.draw.rect(screen, colors[(row + col) % 2], pygame.Rect(x, y, tile_width, tile_width))

#Check for intersection
def intersect(first_p, second_p, x, y):
    return any(x == i.X and y == i.Y for i in first_p) or any(x == i.X and y == i.Y for i in second_p)

#Check for hitting the wall
def hitWall(first_p, second_p):
    return any(second_p[0].X == i.X and second_p[0].Y == i.Y for i in first_p)

    
#Initials for food timer
last_tick = pygame.time.get_ticks()
seconds = 6

#Main game function
def game_loop():
    global seconds
    global last_tick

    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()
    end_im = pygame.image.load("images/end.png")
    

    # Initialize game objects
    worm = Worm(20)
    wall = Wall(20)
    limit = 0
    speed = 5
    end = False
    done = False
    score = 0
    
    #Set up the font
    font = pygame.font.Font(None, 36)
 
    
    #Main game loop
    while not done:
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if end:  #If game is over, show game over screen
                screen.fill((0, 0, 0))  #Clear the screen to black
                screen.blit(end_im, (0, 0))  #Show game over image
                pygame.display.flip()

        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        done = True  #Quit game
                    elif event.key == pygame.K_r:
                        #Reset the game
                        worm = Worm(20)
                        wall = Wall(20)
                        limit = 0
                        speed = 5
                        end = False
                        #Continue the loop
            else:
                filtered_events.append(event)

        
        if not end:
            #Spawn food
            if not limit:
                asorti = random.randint(1, 3)
                while True:
                    x = random.randrange(0, 400, 20)
                    y = random.randrange(0, 300, 20)
                    if not intersect(worm.points, wall.points, x, y):
                        break
                food = Food(x, y, 20, screen, asorti)
                food_stime = pygame.time.get_ticks()
                
           
                limit = 1

            

            if pygame.time.get_ticks() - food_stime >= 6000:
                food.disappear()
                limit = 0
                food_stime = pygame.time.get_ticks()
                seconds = 6

            worm.process_input(filtered_events)
            worm.move()

            #Check for if touching the walls
            if hitWall(wall.points, worm.points):
                end = True  #Set the end checker 

            worm.points[0].X %= 400
            worm.points[0].Y %= 300

            #Check if worm eats food
            pos = food.can_eat(worm.points[0])
            if pos:
                worm.increase(pos)
                score+=asorti
                limit = 0
                food_stime = pygame.time.get_ticks()
                seconds = 6
                if len(worm.points) % 3 == 0:
                    wall.next_level()
                    speed += 0.5

            #Draw everything
            create_background(screen, 400, 300)

            txt = f"Food goes off in{seconds} seconds"

            if pygame.time.get_ticks() - last_tick >= 1000:
                seconds-=1
                last_tick = pygame.time.get_ticks()

            txt_surface = font.render(txt, True, (0,0,0))
            screen.blit(txt_surface, (150, 0))
         
            if food.points:
                food.fdraw(screen)

            wall.draw(screen)
            worm.draw(screen)
            text = f"Score:{score}"
            text_surface = font.render(text, True, (0, 0, 0))
            screen.blit(text_surface, (0, 0))

        pygame.display.flip()
        clock.tick(speed)


#Main function for restarting
def main():
    game_loop()

main()
