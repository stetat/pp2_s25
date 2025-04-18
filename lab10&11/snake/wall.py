import pygame
from game_object import GameObject 
from game_object import Point 

class Wall(GameObject):

    #Initialize the tile width and first level
    def __init__(self, tile_width):
        super().__init__([],(255,0,0), tile_width)
        self.level = 1
        self.load_level()

    #Represent the level from the file
    def load_level(self):
        f = open("levels/level{}.txt".format(self.level), "r")
        row = -1
        col = -1
        for line in f:
            row = row + 1
            col = -1
            for c in line:
                col = col + 1
                if c == '#':
                    self.points.append(Point(col * self.tile_width, row * self.tile_width))
        f.close()

    #Move to next level, set a boundary of 3 levels
    def next_level(self):
        self.points = []
        self.level = (self.level + 1) % 3
        self.load_level()