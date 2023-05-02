import pygame, sys
from settings import *
from debug import debug
# from level import Level
from level_engine import Level_engine


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Spaceship")
        self.clock = pygame.time.Clock()

        # self.level = Level()
        self.level_engine = Level_engine()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            # self.level.run()
            self.level_engine.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()