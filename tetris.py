from settings import *
import math
from system import System
import pygame.freetype as ft

class Text:
    def __init__(self, app):
        self.app = app
        self.font = ft.Font(FONT_PATH)

    def draw(self):
        self.font.render_to(
            self.app.screen,
            (WIN_W * 0.595, WIN_H * 0.02),
            text='3AM',
            fgcolor='red',
            size=TILE_SIZE * 1.4)

        self.font.render_to(
            self.app.screen,
            (WIN_W * 0.68, WIN_H * 0.08),
            text='TETRO',
            fgcolor='white',
            size=TILE_SIZE * 1.4)

        self.font.render_to(
            self.app.screen,
             (WIN_W * 0.68, WIN_H * 0.22),
            text='NEXT',
            fgcolor='yellow',
            size=TILE_SIZE * 1.4)

        self.font.render_to(
            self.app.screen,
            (WIN_W * 0.68, WIN_H * 0.67),
            text='SCORE',
            fgcolor='yellow',
            size=TILE_SIZE * 1.4)

        self.font.render_to(
            self.app.screen,
            (WIN_W * 0.735, WIN_H * 0.8),
            text=f'{self.app.tetris.score}',
            fgcolor='white',
            size=TILE_SIZE * 1.4)
        

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.system = System(self)
        self.next_system  = System(self, current=False)
        self.speed_up = False

        self.score = 0
        self.full_lines = 0
        self.points_per_lines = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

    def get_score(self):
        self.score += self.points_per_lines[self.full_lines]
        self.full_lines = 0

    def check_full_lines(self):
        row = FIELD_H - 1
        for y in range(FIELD_H - 1, -1, -1):
            if sum(map(bool, self.field_array[y])) < FIELD_W:
                for x in range(FIELD_W):
                    self.field_array[row][x] = self.field_array[y][x]

                    if self.field_array[row][x]:
                        self.field_array[row][x].pos = vec(x, row)
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field_array[y][x].alive = False
                    self.field_array[y][x] = 0 

                self.full_lines += 1 

    def put_system_blocks_in_array(self):
        for block in self.system.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def is_game_over(self):
        if self.system.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(300)
            return True

    def check_system_landing(self):
        if self.system.landing:
            if self.is_game_over():
                self.__init__(self.app)
            else:
                self.speed_up = False
                self.put_system_blocks_in_array()
                self.next_system.current = True
                self.system = self.next_system
                self.next_system = System(self, current=False)

    def control(self, pressed_key):
        if (pressed_key == pg.K_LEFT or pressed_key == pg.K_a):
            self.system.move(direction='left')
        elif (pressed_key == pg.K_RIGHT or pressed_key == pg.K_d):
            self.system.move(direction='right')
        elif (pressed_key == pg.K_UP or pressed_key == pg.K_w):
            self.system.rotate()
        elif (pressed_key == pg.K_DOWN or pressed_key == pg.K_s):
            self.speed_up = True

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speed_up]
        if trigger:
            self.system.update()
            self.check_system_landing()
            self.check_full_lines()
            self.get_score()

        self.sprite_group.update()
  
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)