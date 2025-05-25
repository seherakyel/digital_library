

from fastapi import FastAPI
from routes.users_routes import router as users_routes
app = FastAPI()

app.include_router(users_routes,prefix="users",tags=["Users"])