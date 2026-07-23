from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self, system, pos):
        self.system = system

        super().__init__(system.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('orange')

        self.rect = self.image.get_rect()
        self.rect.topleft = pos[0] * TILE_SIZE, pos[1] * TILE_SIZE

class System:
    def __init__(self, tetris):
        self.tetris = tetris
        Block(self, (4, 7))

    def update(self):
        pass

