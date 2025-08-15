
class BaseResponse:

    def __init__(self, message: str, code: int, status: bool, data = None):
        self.message = message;
        self.code = code;
        self.status = status;
        self.data = data;
    
    @staticmethod
    def ok(message="Ok", data=None):
        return BaseResponse(message, code="200", status = True, data = data);

    @staticmethod
    def error(message="Internal Server Error", code="500"):
        return BaseResponse(message, code, False, None);