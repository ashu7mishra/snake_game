from config.settings import Settings

def main():
    settings = Settings()
    print(f"Screen Width: {settings.screen_width}")
    print(f"Screen Height: {settings.screen_height}")


if __name__ == "__main__":
    main()