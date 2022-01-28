class SingletonConfig:
    _instance = None

    def __new__(cls):
        if not getattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance
