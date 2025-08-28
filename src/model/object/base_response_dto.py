
class BaseResponse:

    def __init__(self, message: str, code: str, status: bool, data = None):
        self.message = message
        self.code = code
        self.status = status
        self.data = data
    
    @staticmethod
    def ok(message="Ok", data=None):
        return BaseResponse(message, code="200", status = True, data = data)

class BaseResponseException(Exception):
    """I don't know why FastAPI requires this type of setup.
    But let's just follow the lead.

    """

    def __init__(self, message: str, status_code: int = 400, error_code: str = ""):
        self.name = message
        self.status_code = status_code
        self.code = error_code

    def error_response(self):
        # return BaseResponse(self.name, self.code, False, None)
        return {
            "status": False,
            "code": self.code,
            "message": self.name,
            "data": None
        }