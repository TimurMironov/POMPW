from fastapi import FastAPI

from backend_services.base_app.database import create_tables
from backend_services.services.user_service import user_service

# create_database_if_not_exists()
create_tables()
# with session_maker() as session:
#     fill_users_tables(session)

app = FastAPI()
app.include_router(user_service.router)


@app.get("/")
def home() -> str:
    return "Welcome home bitch"
