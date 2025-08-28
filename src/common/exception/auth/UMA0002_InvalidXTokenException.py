from model.object import BaseResponseException


class InvalidXTokenException(BaseResponseException):

    def __init__(self):
        self.name = "Invalid X token"
        self.status_code = 403
        self.code = "UMA0002"