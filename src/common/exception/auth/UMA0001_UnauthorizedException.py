from model.object import BaseResponseException


class UnauthorizedException(BaseResponseException):

    def __init__(self):
        self.name = "Unauthorized"
        self.status_code = 401
        self.code = "UMA0001"