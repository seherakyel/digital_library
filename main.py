

from fastapi import FastAPI
from routes.users_routes import router as users_routes
app = FastAPI()



from fastapi import FastAPI
from routes.users_routes import router as users_routes

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Uygulama çalışıyor"}

app.include_router(users_routes,prefix="/users",tags=["Users"])