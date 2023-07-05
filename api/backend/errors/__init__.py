class ConfigError(Exception):
    def __init__(self):
        super().__init__("Invalid config file or not found!")
