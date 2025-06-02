

from fastapi import FastAPI
from routes.users_routes import router as users_routes
from routes.books_routes import router as books_routes
from routes.ratings_routes import router as ratings_routes
from routes.categories_routes import router as categories_routes
from routes.favorites_routes import router as favorites_routes
from routes.comments_routes import router as comments_routes
app = FastAPI()


app.include_router(users_routes,prefix="/users",tags=["Users"])
app.include_router(books_routes,prefix="/books",tags=["Books"])
app.include_router(ratings_routes,prefix="/ratings",tags=["Ratings"])
app.include_router(categories_routes,prefix="/categories",tags=["Categories"])
app.include_router(favorites_routes,prefix="/favorites",tags=["Favrorites"])
app.include_router(comments_routes,prefix="/comments",tags=["Comments"])