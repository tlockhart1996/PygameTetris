import pygame
from piece import Piece
import tile
from tile import Tile
WIDTH = 300


class IPiece(Piece):
    def __init__(self, startx=WIDTH//Tile.sidelength//2):
        Piece.__init__(self)
        self.tiles.append(Tile(startx, 2, (10, 100, 240)))
        self.tiles.append(Tile(startx, 0, (0, 0, 0, 100)))
        self.tiles.append(Tile(startx, 1, (0, 0, 0, 100)))
        self.tiles.append(Tile(startx, 3, (0, 0, 0, 100)))
