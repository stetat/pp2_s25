import pygame
from game_object import GameObject 
from game_object import Point 

#Class for worm (snake)
class Worm(GameObject):
    def __init__(self, tile_width):
        super().__init__([Point(20, 20)],(0,0,255), tile_width)
        self.DX = 1
        self.DY = 0
        

    #Move the worm according to current direction
    def move(self):
        
        for i in range(len(self.points) - 1, 0, -1):
            self.points[i].X = self.points[i - 1].X
            self.points[i].Y = self.points[i - 1].Y

        self.points[0].X +=  self.DX * self.tile_width
        self.points[0].Y +=  self.DY * self.tile_width

    #Draw the tiles. The head is dark gray
    def draw(self, screen):

        for i, point in enumerate(self.points):
            if i == 0:  
                color = (77, 77, 77)  
            else:
                color = self.color 

            pygame.draw.rect(screen, color, pygame.Rect(point.X, point.Y, self.tile_width, self.tile_width))

    #Increase worm's length
    def increase(self, pos):
        self.points.append(Point(pos.X, pos.Y))


    #Process user's action and change direction
    def process_input(self,  events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.DX = 0
                self.DY = -1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.DX = 0
                self.DY = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.DX = 1
                self.DY = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.DX = -1
                self.DY = 0