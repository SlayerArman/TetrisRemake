from settings import *
import math
from system import System

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.system = System(self)

    def put_system_blocks_in_array(self):
        for block in self.system.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def check_system_landing(self):
        if self.system.landing:
            self.put_system_blocks_in_array()
            self.system = System(self)

    def control(self, pressed_key):
        if (pressed_key == pg.K_LEFT or pressed_key == pg.K_a):
            self.system.move(direction='left')
        elif (pressed_key == pg.K_RIGHT or pressed_key == pg.K_d):
            self.system.move(direction='right')
        elif (pressed_key == pg.K_UP or pressed_key == pg.K_w):
            self.system.rotate()

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        if self.app.anim_trigger:
            self.system.update()
            self.check_system_landing()
        self.sprite_group.update()
  
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)