class Settings:
    """
    Singleton class for storing game configurations."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance
    
    def initialize(cls):
        """Initialize default settings."""
        cls.screen_width = 800
        cls.screen_height = 600
        cls.bg_color = (0, 0, 0)  # Black background
        cls.ship_speed = 1.5
        cls.bullet_speed = 3.0
        cls.alien_speed = 1.0
        cls.fleet_drop_speed = 10
        cls.fleet_direction = 1  # 1 for right, -1 for left