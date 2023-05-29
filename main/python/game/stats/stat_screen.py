from settings import *
import pygame
from stats.stat_saver import get_stats

class Stat_screen:
    def __init__(self) -> None:
        self.data = get_stats()
        self.results_text = self.convert_data_to_string()
        self.ext = False
        self.clock = pygame.time.Clock()

        self.display_surface = pygame.display.get_surface()
        self.background_image = pygame.image.load('main/python/resources/background_image.jpg').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))
        self.bg_tiles = 2
        self.scroll = 0
        self.bg_height = HEIGHT

    def update_stats(self):
        if len(self.data) == get_stats():
            return
        
        self.data = get_stats()
        self.results_text = self.convert_data_to_string()

    def convert_data_to_string(self):
        output = "TOP RESULTS!\n"
        for player, score in self.data[:5]:
            output += player + " --> " + str(score) + "\n"

        output += "\n"
        output += "PRESS ESC\n"
        output += "TO RETURN TO MENU"
        return output
    
    def draw_background(self):

        for i in range(2):
            self.display_surface.blit(self.background_image, (0, -i * self.bg_height + self.scroll))

        self.scroll += 2

        if abs(self.scroll) > self.bg_height:
            self.scroll = 0

    def draw_stats(self):
        font = pygame.font.Font(GAME_FONT, 64)
        self.blit_text(self.display_surface, self.results_text, (WIDTH//2, 100), font)


    def blit_text(self, surface, text, pos, font, color=FONT_COLOR):
        lines = text.splitlines()
        x, y = pos
        for line in lines:
            if line == "\n":
                y += 20
            line_surface = font.render(line, 0, color)
            line_width, line_height = line_surface.get_size()
            surface.blit(line_surface, (x - line_width//2, y))
            y += line_height + 10


    def run(self):
        while not self.ext:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.ext = True

            if keys[pygame.K_ESCAPE]:
                self.ext = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.update_stats()
            self.draw_background()
            self.draw_stats()
            pygame.display.update()
            self.clock.tick(FPS)
            
