from fastapi import FastAPI

from backend_services.endpoints.users import user_service

app = FastAPI()

app.include_router(user_service.router)

@app.get("/")
def home() -> str:
    return "Welcome home bitch"