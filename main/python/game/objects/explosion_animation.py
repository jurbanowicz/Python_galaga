import pygame

class Animation:
    def __init__(self, screen, position, width) -> None:
        self.image = pygame.image.load("main/python/resources/Explosion.png")
        
        # set new image size width should be 12 * height
        self.height = width * 1.25
        self.width = width * 1.25

        self.image = pygame.transform.scale(self.image, (12*self.width, self.height)) # resize the image
        self.screen = screen
        self.position = position
        self.curr_frame = 0
        self.curr_ticks = 0
        self.ticks_per_frame = 2

    def display_explosion(self):
        '''Run the next frames of the explosion animation. If animation has ifnished, return 1'''
        if self.curr_frame == 12:
            return 1
        subsurface = self.image.subsurface(pygame.Rect(self.curr_frame*self.width, 0, self.width, self.height))
        self.screen.blit(subsurface, self.position)

        self.curr_ticks += 1
        if self.curr_ticks > self.ticks_per_frame:
            self.curr_ticks = 0
            self.curr_frame += 1

        return 0


# clock = pygame.time.Clock()
# pygame.init()
# screen_width, screen_height = 800, 600  # Adjust the values as per your needs
# screen = pygame.display.set_mode((screen_width, screen_height))

# animation = Animation(screen, (0,0))

# running = True
# while running:
#     screen.fill((0, 0, 0))  # Clear the screen before drawing the next frame

#     # Draw the subsurface on the screen
#     animation.display_explosion()

#     pygame.display.flip()  # Update the display
#     clock.tick(60)

    
#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False