from config.settings import Settings
from ui.renderer import Renderer
from ui.game_screen import GameScreen
import pygame

def main():
    renderer = Renderer()
    game_screen = GameScreen(renderer)
    settings = Settings()

    running = True

    snake_body = [(100, 100), (80, 100), (60, 100)]

    snake_food = (200, 200)

    clock = pygame.time.Clock()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        renderer.clear_screen()
        game_screen.draw_snake(snake_body)
        game_screen.draw_food(snake_food)
        renderer.update_screen()

        clock.tick(settings.fps)  # Control the frame rate


if __name__ == "__main__":
    main()