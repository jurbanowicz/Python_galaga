import pygame

class Boundary(pygame.sprite.Sprite):

    def __init__(self, 
                 position: tuple, 
                 groups: list) -> None:
        
        super().__init__(groups)
        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect(topleft=position)
        self.rect.width = 1 