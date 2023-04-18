import pygame
from settings import *
from math import ceil
from random import randint

from objects.player import Player
from objects.enemy import Enemy
from objects.missle import Missle


from debug import debug

class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.spaceship_sprites = pygame.sprite.Group()
        self.booster_sprites = pygame.sprite.Group()
        self.enemies_sprites = pygame.sprite.Group()
        self.missle_sprites = pygame.sprite.Group()
        
        self.font = pygame.font.Font(None, 30)
        self.background_image = pygame.image.load('main/python/resources/background_image.jpg').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))
        self.bg_tiles = 2
        self.scroll = 0
        self.bg_height = HEIGHT
        
        self.create_map()

    def create_map(self) -> None:
        self.player = Player((0, 0), [self.visible_sprites, self.spaceship_sprites], self.missle_sprites, self.booster_sprites)
        # self.enemies = [Enemy((WIDTH/2,70), [self.visible_sprites, self.enemies_sprites, self.spaceship_sprites], 'basic', self.missle_sprites)]
        self.generate_enemies(3)

    def generate_enemies(self, n: int):
        for i in range(n):
            self.enemies_sprites.add((Enemy((randint(30, WIDTH-30), 70), [self.visible_sprites, self.enemies_sprites, self.spaceship_sprites], 'basic', self.missle_sprites)))

    def draw_background(self):

        for i in range(2):
            self.display_surface.blit(self.background_image, (0, -i * self.bg_height + self.scroll))

        self.scroll += 2

        if abs(self.scroll) > self.bg_height:
            self.scroll = 0

    def fire_missle(self, position,  direction = -1):
        missle = Missle((position[0], position[1]), [], 'basic', direction, self.spaceship_sprites)
        self.missle_sprites.add(missle)
        self.visible_sprites.add(missle)

    def check_missle_fired(self):
        if self.player.shot_fired:
            pos = self.player.get_position()
            self.fire_missle((pos[0], pos[1] - 50))
            self.player.shot_fired = False

    def check_missle_collistion(self):
        for sprite in self.missle_sprites:
            if not sprite.exists:
                self.missle_sprites.remove(sprite)
                self.visible_sprites.remove(sprite)
        for sprite in self.enemies_sprites:
            if not sprite.exists:
                self.enemies_sprites.remove(sprite)
                self.spaceship_sprites.remove(sprite)
                self.visible_sprites.remove(sprite)
                self.player.score += 10

    def display_score(self):
        score_string = "Score: " + str(self.player.score)
        score = self.font.render(score_string, True, (255, 255, 255))
        score_rect = score.get_rect()
        score_rect.center = WIDTH - 50 , 35
        self.display_surface.blit(score, score_rect)

    def enemies_shoot(self):
        for enemy in self.enemies_sprites:
            if enemy.shot_fired:
                pos = enemy.get_position()
                self.fire_missle((pos[0], pos[1] + 50), 1)
                enemy.shot_fired = False


    def run(self) -> None:

        self.draw_background()
        self.visible_sprites.draw(self.display_surface)
        print(len(self.missle_sprites))
        self.check_missle_fired()
        self.enemies_shoot()
        self.check_missle_collistion()
        self.display_score()
        self.visible_sprites.update()
        if len(self.enemies_sprites) == 0:
            self.generate_enemies(3)

        stats = [enemy.life for enemy in self.enemies_sprites]
        debug(self.player.life)
