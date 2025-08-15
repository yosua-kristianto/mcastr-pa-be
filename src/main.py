from fastapi import FastAPI
from routes.routes import route

app = FastAPI()
app.include_router(route)

print("Core Service is running")
print("""
 |  \\/  |        /\\       | |        |  __ \\ /\\     |  _ \\|  ____|
 | \\  / | ___   /  \\   ___| |_ _ __  | |__) /  \\    | |_) | |__   
 | |\\/| |/ __| / /\\ \\ / __| __| '__| |  ___/ /\\ \\   |  _ <|  __|  
 | |  | | (__ / ____ \\\\__ \\ |_| |    | |  / ____ \\  | |_) | |____ 
 |_|  |_|\\___/_/    \\_\\___/\\__|_|    |_| /_/    \\_\\ |____/|______|
                                                                  
                                                                  
""")