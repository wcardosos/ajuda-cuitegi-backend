from src.errors.BaseError import BaseError


class InvalidRequestBodyError(BaseError):
    def __init__(self, message: str):
        super(InvalidRequestBodyError, self).__init__(message)