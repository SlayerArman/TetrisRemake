from settings import *
import math
import json
import os
import random
from system import System
import pygame.freetype as ft

SCORE_FILE = os.path.join(os.path.abspath("."), "highscore.json")

def load_high_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f).get("high_score", 0)
    return 0

def save_high_score(score, high_score):
    if score >= high_score:
        with open(SCORE_FILE, "w") as f:
            json.dump({"high_score": score}, f)
        return score
    return high_score


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
            (WIN_W * 0.61, WIN_H * 0.50),
            text='HI-SCORE',
            fgcolor='yellow',
            size=TILE_SIZE * 1.2)

        self.font.render_to(
            self.app.screen,
            (WIN_W * 0.7, WIN_H * 0.58),
            text=f'{self.app.tetris.high_score}',
            fgcolor='white',
            size=TILE_SIZE * 1.3)

        self.font.render_to(
            self.app.screen,
            (WIN_W * 0.66, WIN_H * 0.70),
            text='SCORE',
            fgcolor='yellow',
            size=TILE_SIZE * 1.3)

        self.font.render_to(
            self.app.screen,
            (WIN_W * 0.7, WIN_H * 0.79),
            text=f'{self.app.tetris.score}',
            fgcolor='white',
            size=TILE_SIZE * 1.4)


class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.system = System(self)
        self.next_system = System(self, current=False)
        self.speed_up = False

        self.score = 0
        self.high_score = load_high_score()
        self.full_lines = 0
        self.points_per_lines = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}
        
        self.particles = []

    def get_score(self):
        self.score += self.points_per_lines[self.full_lines]
        self.full_lines = 0
        if self.score > self.high_score:
            self.high_score = self.score

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
            self.high_score = save_high_score(self.score, self.high_score)
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
                pg.draw.rect(self.app.screen, (20, 20, 20),
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update_particles(self):
        spawn_chance = 0.8 if self.speed_up else 0.25
        if self.system.current and random.random() < spawn_chance:
            for block in self.system.blocks:
                px = (block.pos.x * TILE_SIZE) + random.uniform(4, TILE_SIZE - 4)
                py = (block.pos.y * TILE_SIZE) + random.uniform(4, TILE_SIZE - 4)
                radius = random.uniform(3, 5)
                vx = random.uniform(-0.4, 0.4)
                vy = random.uniform(-1.2, -0.3)
                self.particles.append([px, py, radius, 255, vx, vy])

        for p in self.particles[:]:
            p[0] += p[4]
            p[1] += p[5]
            p[2] -= 0.08
            p[3] -= 10
            if p[2] <= 0 or p[3] <= 0:
                self.particles.remove(p)

    def draw_particles(self):
        for p in self.particles:
            radius = int(p[2])
            if radius > 0:
                surf = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
                pg.draw.circle(surf, (0, 255, 255, int(p[3])), (radius, radius), radius)
                self.app.screen.blit(surf, (p[0] - radius, p[1] - radius), special_flags=pg.BLEND_RGBA_ADD)

    def draw_ghost_piece(self):
        if self.system.current:
            ghost_positions = self.system.get_ghost_positions()
            for pos in ghost_positions:
                pg.draw.rect(self.app.screen, (110, 110, 110),
                             (pos.x * TILE_SIZE, pos.y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)

    def update(self):
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speed_up]
        if trigger:
            self.system.update()
            self.check_system_landing()
            self.check_full_lines()
            self.get_score()

        self.update_particles()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.draw_ghost_piece()
        self.draw_particles()
        for block in self.sprite_group:
            block.draw_bloom(self.app.screen)
        self.sprite_group.draw(self.app.screen)