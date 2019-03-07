import cv2
import pygame
import time

from tile import Tile

TILE_LENGTH = Tile.sidelength
WIDTH = 300
HEIGHT = 500
BOARD_WIDTH = WIDTH/TILE_LENGTH
BOARD_HEIGHT = HEIGHT/TILE_LENGTH
BG = (255,255,255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG)

tiles = []

tiles.append(Tile(0,0, (0,0,255), 0))
tiles.append(Tile(1,1, (255,0,0), 1))
tiles.append(Tile(2,2, (0,255,0), 2))
def tick():
    screen.fill(BG)
    for tile in tiles:
        tile.update()
        tile.draw(screen)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #30 frames per second
    time.sleep(0.016)
    tick()
