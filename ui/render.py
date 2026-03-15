import pygame
from config.settings import Settings

class Render:
    """Class responsible for rendering game elements on the screen."""
    def __init__(self, screen):
        pygame.init()
        self.settings = Settings()
        
         # Update the full display surface to the screen with the new settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Snake Game')

        def clear_screen(self):
            """Fill the screen with the background color."""
            self.screen.fill(self.settings.bg_color)

        def update_screen(self):
            """Update the screen to show the new frame."""
            pygame.display.update()

        def draw_snake(self, color, x, y, width, height):
            """Draw the snake on the screen."""
            pygame.draw.rect(self.screen, color, (x, y, width, height))