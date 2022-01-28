from .singleton_config import SingletonConfig


class Config(SingletonConfig):
    def __init__(self):
        self.host = "https://test.io/"
        self.driver_path = "./core/infrastructure/bin/chromedriver"
