from settings import *
import math
from system import System

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.system = System(self)

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TILE_SIZE, Y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        self.system.update()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)