from fastapi import FastAPI

from routes.routes import route

app = FastAPI()





from middleware import Authenticate
app.add_middleware(Authenticate)

app.include_router(route)

from model.object import BaseResponseException
from starlette.requests import Request

@app.exception_handler(BaseResponseException)
async def custom_exception_handler(request: Request, exc: BaseResponseException):
    return exc.error_response()

print("Core Service is running")
print("""
 |  \\/  |        /\\       | |        |  __ \\ /\\     |  _ \\|  ____|
 | \\  / | ___   /  \\   ___| |_ _ __  | |__) /  \\    | |_) | |__   
 | |\\/| |/ __| / /\\ \\ / __| __| '__| |  ___/ /\\ \\   |  _ <|  __|  
 | |  | | (__ / ____ \\\\__ \\ |_| |    | |  / ____ \\  | |_) | |____ 
 |_|  |_|\\___/_/    \\_\\___/\\__|_|    |_| /_/    \\_\\ |____/|______|
                                                                  
                                                                  
""")


