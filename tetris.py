import cv2
import pygame
import time
from ipiece import IPiece

from tile import Tile

pygame.font.init()
myfont = pygame.font.SysFont('Palatino', 15)

TILE_LENGTH = Tile.sidelength
WIDTH = 300
HEIGHT = 300
BOARD_WIDTH = WIDTH//TILE_LENGTH
BOARD_HEIGHT = HEIGHT//TILE_LENGTH
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

tiles = []

# tiles.append(Tile(0, 0, (0, 0, 255), 0))
# tiles.append(Tile(1, 1, (255, 0, 0), 1))
# tiles.append(Tile(2, 2, (0, 255, 0), 2))

pieces = []

pieces.append(IPiece())
# pieces.append(IPiece(1))


def draw_board():
    for i in range(BOARD_WIDTH):
        pygame.draw.line(screen, BLACK, (i*TILE_LENGTH, 0),
                         (i*TILE_LENGTH, HEIGHT))

    for i in range(BOARD_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, i*TILE_LENGTH),
                         (WIDTH, i*TILE_LENGTH))

    # for y in range(BOARD_HEIGHT):
    #     for x in range(BOARD_WIDTH):
        # ts = myfont.render('{},{}'.format(
        #     x + 1, y + 1), False, (10, 10, 10))
        # screen.blit(ts, (x * TILE_LENGTH + TILE_LENGTH /
        #                  2, y*TILE_LENGTH + TILE_LENGTH/2))

        # ts = myfont.render('x: {},  y: {}'.format(
        #     x - 1, y - 1), False, (10, 10, 10))
        # screen.blit(ts, (x * TILE_LENGTH + TILE_LENGTH /
        #                  2 - 20, y*TILE_LENGTH + TILE_LENGTH/2))


def tick():
    screen.fill(WHITE)
    # draw_board()
    print(pieces)
    print(tiles)
    for tile in tiles:
        tile.draw(screen)

    for piece in pieces:
        piece.update()
        piece.draw(screen)

    for piece in pieces:
        for tile in piece.tiles:
            if tile.y == BOARD_HEIGHT - 1:
                piece.finish()
                break

    for i in range(len(pieces) - 1, -1, -1):
        if pieces[i].finished:
            for tile in pieces[i].tiles:
                tiles.append(tile)
            del pieces[i]

    if pieces[0]:
        pieces[0].rotate_clockwise()
    pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 30 frames per second
    time.sleep(0.016)
    time.sleep(.5)
    tick()
