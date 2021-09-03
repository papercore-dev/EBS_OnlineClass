class EOCException(Exception):
    pass


class EmptyArguments(EOCException):
    def __init__(self, message: str):
        super().__init__(message)
