import pygame


class Piece:
    def __init__(self):
        self.tiles = []
        self.finished = False
        # origin of the piece is the first element in the array

    def rotate_clockwise(self):
        for i in range(len(self.tiles)):
            self.tiles[i].x *= -1
            self.tiles[i].y *= -1

        xoffset = self.tiles[0].x
        yoffset = self.tiles[0].y

        for i in range(len(self.tiles)):
            self.tiles[i].x - xoffset
            self.tiles[i].y - yoffset

        for i in range(len(self.tiles)):
            self.tiles[i].move_clockwise()

        for i in range(len(self.tiles)):
            self.tiles[i].x + xoffset
            self.tiles[i].y + yoffset

        for i in range(len(self.tiles)):
            self.tiles[i].x *= -1
            self.tiles[i].y *= -1

    def rotate_counter_clockwise(self):
        for i in range(len(self.tiles)):
            self.tiles[i].x *= -1
            self.tiles[i].y *= -1

        xoffset = self.tiles[0].x
        yoffset = self.tiles[0].y

        for i in range(len(self.tiles)):
            self.tiles[i].x - xoffset
            self.tiles[i].y - yoffset

        for i in range(len(self.tiles)):
            self.tiles[i].move_counter_clockwise()

        for i in range(len(self.tiles)):
            self.tiles[i].x + xoffset
            self.tiles[i].y + yoffset

        for i in range(len(self.tiles)):
            self.tiles[i].x *= -1
            self.tiles[i].y *= -1

    def move_down(self):
        pass

    def update(self):
        print("updating")
        if not self.finished:
            for tile in self.tiles:
                tile.update()

    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)

    def finish(self):
        for i in range(len(self.tiles)):
            self.tiles[i].finished = True
        self.finished = True
