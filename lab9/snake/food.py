import pygame
import random
from game_object import GameObject 
from game_object import Point 
from wall import Wall
from worm import Worm

#Check for intersections
def intersect(wall_p, worm_p, x, y):
    for i in wall_p:
        if x == i[0] or y == i[1]:
            return True

    for i in worm_p:
        if x == i[0] or y == i[1]:
            return True
    
    return False

#Upload images
baursaq = pygame.image.load("images/baursaq.png")
qurt = pygame.image.load("images/qurt.png")
qazy = pygame.image.load("images/qazy.png")
    

#Define class for Food
class Food(GameObject):

    
    
    #Passing food count and screen as arguments
    def __init__(self, x, y, tile_width, screen, asorti):
        
        super().__init__([Point(x, y)],(255,255,255), tile_width)
        self.asorti = asorti
        self.screen = screen

    #Draw different types of food
    def fdraw(self, screen):
        
        x, y = self.points[0].X, self.points[0].Y

        if self.asorti == 1:
            screen.blit(baursaq, (x, y))
        elif self.asorti == 2:
            screen.blit(qurt, (x, y))
        elif self.asorti == 3:
            screen.blit(qazy, (x, y))

    #Remove food
    def disappear(self):
        self.points = []

     
        
    #Check if worm's head collides with food
    def can_eat(self, head_location):
     
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
               
                break
        return result

    