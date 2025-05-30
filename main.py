

from fastapi import FastAPI
from routes.users_routes import router as users_routes
from routes.books_routes import router as books_routes
from routes.ratings_routes import router as ratings_routes
app = FastAPI()


app.include_router(users_routes,prefix="/users",tags=["Users"])
app.include_router(books_routes,prefix="/books",tags=["Books"])
app.include_router(ratings_routes,prefix="/ratings",tags=["Ratings"])