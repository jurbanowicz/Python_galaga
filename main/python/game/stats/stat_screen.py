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

        output += "PRESS ENTER TO PLAY AGAIN"
        return output
    
    def draw_background(self):

        for i in range(2):
            self.display_surface.blit(self.background_image, (0, -i * self.bg_height + self.scroll))

        self.scroll += 2

        if abs(self.scroll) > self.bg_height:
            self.scroll = 0

    def draw_stats(self):
        font = pygame.font.SysFont('freesansbold.ttf', 100)
        self.blit_text(self.display_surface, self.results_text, (WIDTH//5, 100), font)


    def blit_text(self, surface, text, pos, font, color=pygame.Color('red')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height + 10 # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height + 10 # Start on new row.


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
            
