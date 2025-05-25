import sys
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from models.ratings import (  
                     add_rating,get_ratings_by_book_id,get_average_rating_for_book,get_user_rating_for_book
                          
    )
router = APIRouter()

class AddRatingsRequest(BaseModel):
    user_id:int
    book_id:int
    rating:int
    comment:str

class UpdateRatingsRequest(BaseModel): 
    ratings_id:int
    user_id:Optional[int]
    book_id:Optional[int]
    rating:Optional[int]
    comment:Optional[str]




		
