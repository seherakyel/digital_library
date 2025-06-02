import sys
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from models.favorites import ( 
    add_favorites_book,get_favorites_by_user_id,all_book_favorites_by_user,remove_favorites_book) 

router = APIRouter()
class AddFavoriteRequest(BaseModel):
    user_id: int
    book_id: int

@router.post("/add_favorite")
async def add_favorite_endpoint(fav_data: AddFavoriteRequest):
    try:
        result = add_favorites_book(fav_data.user_id, fav_data.book_id)
        if result is None:
            return JSONResponse(content={"message": "Kitap zaten favorilerde."})
        return JSONResponse(content={"message": f"Kitap favorilere eklendi."})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")


@router.get("/favorites/{user_id}")
async def get_favorites_by_user_id_endpoint(user_id: int):
    try:
        favorites = get_favorites_by_user_id(user_id)
        return {"message": "Kullanıcının favorileri getirildi", "data": favorites}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")


@router.get("/all_favorites/{user_id}")
async def all_book_favorites_by_user_endpoint(user_id: int):
    try:
        favorites = all_book_favorites_by_user(user_id)
        return {"message": "Kullanıcının tüm favori kitapları getirildi", "data": favorites}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")


@router.delete("/remove_favorite")
async def remove_favorite_endpoint(fav_data: AddFavoriteRequest):
    try:
        remove_favorites_book(fav_data.user_id, fav_data.book_id)
        return {"message": f"Kitap favorilerden kaldırıldı"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"hata:{str(e)}")