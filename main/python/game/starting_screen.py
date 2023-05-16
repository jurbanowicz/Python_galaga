import pygame, sys
from settings import *
from start_button import start_button
from level_engine import Level_engine
from stats.stat_screen import Stat_screen

class starting_screen:
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()

        self.display_surface = pygame.display.get_surface()
        self.background_image = pygame.image.load('main/python/resources/background_image.jpg').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))
        self.bg_tiles = 2
        self.scroll = 0
        self.bg_height = HEIGHT

        self.start_game = False
        self.show_stats = False
        self.create_buttons()

    def draw_background(self):

        for i in range(2):
            self.display_surface.blit(self.background_image, (0, -i * self.bg_height + self.scroll))

        self.scroll += 2

        if abs(self.scroll) > self.bg_height:
            self.scroll = 0

    def create_buttons(self):
        font = pygame.font.Font(GAME_FONT, 64)
        self.text_start = font.render("START", True, FONT_COLOR)
        self.text_stats = font.render("SCORES", True, FONT_COLOR)

        self.start_rect = self.text_start.get_rect()
        self.stat_rect = self.text_stats.get_rect()

        self.start_rect.center = (WIDTH//4, HEIGHT//2)
        self.stat_rect.center = (3*WIDTH//4 , HEIGHT//2)

    def draw_buttons(self):
        self.display_surface.blit(self.text_start, self.start_rect)
        self.display_surface.blit(self.text_stats, self.stat_rect)

    def check_click(self):
        pos = pygame.mouse.get_pos()

        if (self.start_rect.collidepoint(pos)):
            self.start_game = True

        if (self.stat_rect.collidepoint(pos)):
            self.show_stats = True

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click()
                

            self.draw_background()

            # Level_engine().run()
            # Stat_screen().run()
            self.draw_buttons()

            if self.start_game:
                Level_engine().run()
                self.start_game = False
            
            if self.show_stats:
                Stat_screen().run()
                self.show_stats = False

            self.clock.tick(FPS)
            pygame.display.update()



    