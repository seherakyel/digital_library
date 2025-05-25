import sys
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from models.ratings import (  
                     add_rating,get_ratings_by_book_id,get_average_rating_for_book,get_user_rating_for_book,update_rating
                          
    )
router = APIRouter()

class AddRatingRequest(BaseModel):
    user_id:int
    book_id:int
    rating:int
    comment:Optional[str]

class UpdateRatingRequest(BaseModel): 
    ratings_id:int
    user_id:Optional[int]
    book_id:Optional[int]
    rating:Optional[int]
    comment:Optional[str]



@router.post("/add_rating")
async def add_rating_endpoint(rating_data: AddRatingRequest):
    try:
        add_rating(rating_data.user_id, rating_data.book_id, rating_data.rating, rating_data.comment)
        return JSONResponse(content={"message": "Puan ve yorum başarıyla eklendi."})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")


@router.get("/ratings/{book_id}")
async def get_ratings_by_book_id_endpoint(book_id: int):
    try:
        ratings = get_ratings_by_book_id(book_id)
        return {"message": "Kitaba ait puanlar getirildi", "data": ratings}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")



@router.get("/average_rating/{book_id}")
async def get_average_rating_for_book_endpoint(book_id: int):
    try:
        avg_rating = get_average_rating_for_book(book_id)
        return {"message": "Kitabın ortalama puanı getirildi", "average_rating": avg_rating}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")



@router.get("/user_rating/{user_id}/{book_id}")
async def get_user_rating_for_book_endpoint(user_id: int, book_id: int):
    try:
        user_rating = get_user_rating_for_book(user_id, book_id)
        if user_rating:
            return {"message": "Kullanıcının puanı getirildi", "data": user_rating}
        else:
            return {"message": "Kullanıcı bu kitap için henüz puan vermemiş", "data": None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")



@router.put("/update_rating")
async def update_rating_endpoint(rating_data: UpdateRatingRequest):
    try:
        update_rating(
            rating_data.user_id,
            rating_data.book_id,
            rating_data.new_rating,
            rating_data.new_comment
        )
        return JSONResponse(content={"message": "Puan ve yorum başarıyla güncellendi."})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")



		
