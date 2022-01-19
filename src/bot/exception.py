class BotError(Exception):
    pass

class DependencyNotFoundError(ImportError):
    pass