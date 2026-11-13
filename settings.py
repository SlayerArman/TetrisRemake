import os
import sys
import pygame as pg

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (255, 255, 255)
BG_COLOR = (20, 20, 20)
BACKGROUND_IMAGE_PATH = resource_path('assets/background.png')
MUSIC_PATH = resource_path('assets/music.ogg')
GRID_COLOR = (20, 20, 20)
BLOOM_SIZE = 5
BLOOM_ALPHA = 70

SCORE_FILE = 'highscore.json'
GHOST_COLOR = (110, 110, 110)
PARTICLE_COLOR = (0, 255, 255)

SPRITE_DIR_PATH = resource_path('assets/sprites')
FONT_PATH = resource_path('assets/fonts/fontyboy.ttf')

ANIM_TIME_INTERVAL = 300
FAST_ANIM_TIME_INTERVAL = 15

TILE_SIZE = 30
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.36)
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)} 

SYSTEMS = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}