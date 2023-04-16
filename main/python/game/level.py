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
        self.font = pygame.font.Font(None, 30)
        self.create_map()

    def display_score(self):
        score_string = "Score: " + str(self.player.score)
        score = self.font.render(score_string, True, (255, 255, 255))
        score_rect = score.get_rect()
        score_rect.center = WIDTH - 50 , 35
        self.display_surface.blit(score, score_rect)


    def create_map(self) -> None:
        self.player = Player((0, 0), [self.visible_sprites], self.booster_sprites, self.missle_sprites)
        # for row_index, row in enumerate(WORLD_MAP):
        #     for col_index, col in enumerate(row):
        #         x = col_index * TITLESIZE
        #         y = row_index * TITLESIZE

        #         if col == 'p':
        #             self.player = Player((x, y), [self.visible_sprites], self.boundary_sprites, self.missle_sprites)

        #         if col == 'm':
        #             Missle((x, y), [self.visible_sprites, self.missle_sprites])

        #         if col == 'b':
        #             Booster((x, y), [self.visible_sprites, self.booster_sprites])
        #         if col == 'e':
        #             pass

    def fire_missle(self):
        curr_position = self.player.get_postition()
        missle = Missle((curr_position[0], curr_position[1] - self.player.player_height//2), [])
        self.missle_sprites.add(missle)
        self.visible_sprites.add(missle)

    def check_missle_fired(self):
        if self.player.shot_fired:
            print("Shot registered from level")
            self.fire_missle()
            self.player.shot_fired = False

    def run(self) -> None:

        self.booster_sprites.draw(self.display_surface)
        self.visible_sprites.draw(self.display_surface)
        self.check_missle_fired()
        self.display_score()
        self.visible_sprites.update()

        debug(self.player.direction)