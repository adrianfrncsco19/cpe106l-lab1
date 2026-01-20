# Week 4: Singleton Pattern
# Activity 1
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance


# Optional test to show Singleton behavior
if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    print(logger1 is logger2)  # Should print True


