import pygame
from settings import *
from math import ceil

from debug import debug

class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 30)
        self.background_image = pygame.image.load('main/python/resources/background_image.jpg').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))
        self.bg_tiles = 2
        self.scroll = 0
        self.bg_height = HEIGHT

        self.player = None

    def draw_background(self):

        for i in range(2):
            self.display_surface.blit(self.background_image, (0, -i * self.bg_height + self.scroll))

        self.scroll += 2

        if abs(self.scroll) > self.bg_height:
            self.scroll = 0

    def display_score(self):
        score_string = "Score: " + str(self.player.score)
        score = self.font.render(score_string, True, (255, 255, 255))
        score_rect = score.get_rect()
        score_rect.center = WIDTH - 50 , 35
        self.display_surface.blit(score, score_rect)

    def update(self):
        self.draw_background()
        self.visible_sprites.draw(self.display_surface)
        self.display_score()

        debug(self.player.life)

        pygame.display.update()
        self.clock.tick(FPS)

        
