import pygame
from settings import *

class start_button:
    def __init__(self) -> None:
        self.position = 0, 0
        self.image = pygame.image.load('main/python/resources/start_image.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 200))
        self.start_rect = self.image.get_rect(topleft = self.position)
        print(self.start_rect)


    def draw_button(self, screen):
        screen.blit(self.image, self.start_rect.center)

    def check_click(self) -> bool:
        x, y = pygame.mouse.get_pos()
        print(f'X: {x} y: {y}')
        if self.start_rect.collidepoint(x, y):
            print("BUTTON PRESSED")
            return True
        return False
    
    def update(self, screen) -> bool:
        self.draw_button(screen)