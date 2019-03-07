import pygame
import time
from math import cos, sin, pi

WIDTH = 300
HEIGHT = 300


class Tile:
    sidelength = 30

    def __init__(self, x=0, y=0, color=(0, 0, 0), offset=0):
        self.x = x
        self.y = y
        self.finished = False
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.x * Tile.sidelength, self.y * Tile.sidelength, Tile.sidelength, Tile.sidelength), 4)

    def move_down(self):
        if not self.finished:
            self.update()
            self.update()

    def update(self):
        if not self.finished:
            self.y += 1

    def move_clockwise(self):
        self.move_counter_clockwise()
        self.move_counter_clockwise()
        self.move_counter_clockwise()

    def move_counter_clockwise(self):
        oldx, oldy = self.x, self.y
        self.x = oldx * cos(pi/2) - oldy * sin(pi/2)
        self.y = oldx * sin(pi/2) + oldy * cos(pi/2)
