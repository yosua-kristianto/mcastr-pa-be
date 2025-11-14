from fastapi import FastAPI

from routes.routes import route

app = FastAPI()

from middleware import Authenticate
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(Authenticate)

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


