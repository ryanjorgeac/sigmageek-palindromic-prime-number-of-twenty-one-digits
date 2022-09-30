class Either:
    def process(self, onSuccess, onError):
        raise NotImplementedError()

class Right(Either):
    def __init__(self, value):
        self.value = value

    def process(self, onSuccess, onError):
        onSuccess(self.value)

class Left(Either):
    def __init__(self, error):
        self.error = error

    def process(self, onSuccess, onError):
        onError(self.error)