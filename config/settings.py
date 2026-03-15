import json
from pathlib import Path


class Settings:
    """Singleton class for storing game configurations."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(cls):
        """Initialize default settings."""
        # Defaults (fallback values)
        cls.screen_width = 800
        cls.screen_height = 600
        cls.bg_color = (0, 0, 0)  # Black background

        cls.snake_block_size = 20
        cls.snake_color = (0, 255, 0)  # Green snake

        cls.food_block_size = 20
        cls.food_color = (255, 0, 0)  # Red food

        cls.fps = 15

        # Try loading overrides from game_config.json
        try:
            config_path = Path(__file__).resolve().parent.parent / "game_config.json"
            with config_path.open("r", encoding="utf-8") as f:
                cfg = json.load(f)

            screen = cfg.get("screen", {})
            cls.screen_width = screen.get("width", cls.screen_width)
            cls.screen_height = screen.get("height", cls.screen_height)

            game = cfg.get("game", {})
            cls.snake_block_size = game.get("snake_block_size", game.get("block_size", cls.snake_block_size))
            cls.food_block_size = game.get("food_block_size", game.get("block_size", cls.food_block_size))
            cls.fps = game.get("fps", cls.fps)

            colors = cfg.get("colors", {})
            cls.bg_color = tuple(colors.get("black", cls.bg_color))
            cls.snake_color = tuple(colors.get("green", cls.snake_color))
            cls.food_color = tuple(colors.get("red", cls.food_color))
        except Exception:
            # If config loading fails, keep defaults.
            print("Warning: Could not load game_config.json. Using default settings.")
            pass
