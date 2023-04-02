import pygame
from settings import *
from objects.Booster import Booster
from objects.Boundary import Boundary
from objects.Missle import Missle

from objects.Player import Player



from debug import debug

class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

        
        self.visible_sprites = pygame.sprite.Group()
        
        self.boundary_sprites = pygame.sprite.Group()

        self.booster_sprites = pygame.sprite.Group()
        self.enemys_sprites = pygame.sprite.Group()
        self.missle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self) -> None:
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TITLESIZE
                y = row_index * TITLESIZE
                

                if col == 'x':
                    Boundary((x, y), [self.boundary_sprites])

                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.boundary_sprites, self.missle_sprites)

                if col == 'm':
                    Missle((x, y), [self.visible_sprites, self.missle_sprites])

                if col == 'b':
                    Booster((x, y), [self.visible_sprites, self.booster_sprites])
                if col == 'e':
                    pass

    def run(self) -> None:
        self.booster_sprites.draw(self.display_surface)

        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()

        debug(self.player.direction)