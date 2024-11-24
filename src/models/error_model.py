

class GetError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ValidationError(GetError):
    def __init__(self, message, model):
        super().__init__(message)
        self.model = model


class AuthenticationError(GetError):
    def __init__(self, message, model = None):
        super().__init__(message)
        self.model = model


class SourceNotFoundError(GetError):
    def __init__(self, id):
        super().__init__(f"We don't have vacation with id: {id}")
        self.id = id