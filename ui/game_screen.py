from config.settings import Settings
from ui.renderer import Renderer


class GameScreen:
    """Class responsible for managing the game screen."""
    def __init__(self, renderer):
        self.renderer = renderer
        self.settings = Settings()

    def draw_snake(self, snake_body):
        """Draw the snake on the screen."""
        for segment in snake_body:
            self.renderer.draw_snake(self.settings.snake_color, 
                                     segment[0], 
                                     segment[1], 
                                     self.settings.snake_block_size, 
                                     self.settings.snake_block_size)
            
    def draw_food(self, food_position):
        """Draw the food on the screen."""
        self.renderer.draw_snake(self.settings.food_color, 
                                 food_position[0], 
                                 food_position[1], 
                                 self.settings.food_block_size, 
                                 self.settings.food_block_size)