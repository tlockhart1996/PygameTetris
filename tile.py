import pygame
import time

WIDTH = 300
HEIGHT = 500

class Tile:
    sidelength = 10
    def __init__(self, x = 0, y = 0, color = (0,0,0), offset = 0):
        self.x = x
        self.y = y
        self.color = color
        self.offset = offset
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x * Tile.sidelength, self.y * Tile.sidelength, 10, 10))

    def update(self):
        print(self.x, self.y, self.x * Tile.sidelength, self.y * Tile.sidelength)
        if (self.y + self.offset) * Tile.sidelength + Tile.sidelength < HEIGHT:
            self.y += 1