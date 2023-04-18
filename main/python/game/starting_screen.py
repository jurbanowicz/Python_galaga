import pygame
from settings import *
from start_button import start_button

class starting_screen:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.background_image = pygame.image.load('main/python/resources/background_image.jpg').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))
        self.bg_tiles = 2
        self.scroll = 0
        self.bg_height = HEIGHT

        self.start_button = start_button()
        self.start_game = False


    def draw_background(self):

        for i in range(2):
            self.display_surface.blit(self.background_image, (0, -i * self.bg_height + self.scroll))

        self.scroll += 2

        if abs(self.scroll) > self.bg_height:
            self.scroll = 0

    def run(self):

        self.draw_background()
        self.start_button.update(self.display_surface)
        keys = pygame.key.get_pressed()
        if keys[pygame.MOUSEBUTTONDOWN]:
            print("MOUSEBUTTON DOWN")
            if self.start_button.check_click():
                self.start_game = True


    