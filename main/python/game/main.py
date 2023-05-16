import pygame, sys
from settings import *
from debug import debug
# from level import Level
from level_engine import Level_engine
from stats.stat_screen import Stat_screen
from starting_screen import starting_screen



class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Spaceship")
        self.clock = pygame.time.Clock()


    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 



            self.screen.fill('black')
            starting_screen().run()

            pygame.display.update()




if __name__ == "__main__":
    game = Game()
    game.run()