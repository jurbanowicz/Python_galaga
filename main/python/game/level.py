import pygame
from settings import *
from math import ceil

from debug import debug

class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(GAME_FONT, 30)
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
        score_rect.center = WIDTH - 90 , 20
        self.display_surface.blit(score, score_rect)

    def display_health(self):
        health_string = "HP: " + str(self.player.life)
        health = self.font.render(health_string, True, (255, 255, 255))
        health_rect = health.get_rect()
        health_rect.center = 50 , 20
        self.display_surface.blit(health, health_rect)

    def display_bombs(self):
        bomb_string = "BOMBS: " + str(self.player.missles["bomb"])
        bombs = self.font.render(bomb_string, True, (255, 255, 255))
        bobm_rect = bombs.get_rect()
        bobm_rect.center = 70, 50
        self.display_surface.blit(bombs, bobm_rect)

    def get_end_screen(self, score: int):
        font = pygame.font.Font(GAME_FONT, 64)
        self.text_end = font.render("GAME OVER", True, FONT_COLOR)
        self.text_score = font.render("You scored: " + str(score), True, FONT_COLOR)
        self.text_rect = self.text_end.get_rect()
        self.score_rect = self.text_score.get_rect()
        self.text_rect.center = (WIDTH//2, HEIGHT//3)
        self.score_rect.center = (WIDTH//2, HEIGHT//2)
        self.text_end_2 = font.render("Press ESC to go back", True, FONT_COLOR)
        self.text_2_rect = self.text_end_2.get_rect()
        self.text_2_rect.center = (WIDTH//2, 2*HEIGHT//3)

    def update_end_screen(self):
        self.draw_background()

        self.display_surface.blit(self.text_end, self.text_rect)
        self.display_surface.blit(self.text_score, self.score_rect)
        self.display_surface.blit(self.text_end_2, self.text_2_rect)
        
        pygame.display.update()
        self.clock.tick(FPS)

    def update(self):
        self.draw_background()
        self.visible_sprites.draw(self.display_surface)
        self.display_score()
        self.display_health()
        self.display_bombs()

        # debug(self.player.life)

        pygame.display.update()
        self.clock.tick(FPS)

        
