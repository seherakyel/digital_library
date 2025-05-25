
import sys
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from models.books import (   
    add_books,get_book_by_id,get_all_books,get_books_by_category,delete_books_by_id,update_books,search_books_by_keyword 
    
    )
router = APIRouter()

class AddBooksRequest(BaseModel):
    title: str
    author: str
    description: str
    category_id: int
    published_year: int

class UpdateBooksRequest(BaseModel):
    book_id: int
    title: Optional[str]
    author: Optional[str]
    description: Optional[str]
    category_id: Optional[int]
    published_year: Optional[int]

@router.post("/add_books")
async def add_books_endpoint(books: AddBooksRequest):
    result = add_books(books.title, books.author, books.description,books.category_id, books.published_year)
    if result:
        return JSONResponse(content={"message": f"Kitap '{books.title}' başarıyla eklendi."})
    else:
        raise HTTPException(status_code=400, detail="Kitap eklenemedi.")

@router.get("/books/{books_id}")
async def get_book_by_id_endpoint(books_id: int):
    try:
        book = get_book_by_id(books_id)
        if book:
            return {"message": "Kitap bulundu", "data": book}
        else:
            return {"message": "Kitap bulunamadı", "data": None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")

@router.get("/all_books")
async def get_all_books_endpoint():
    try:
        books = get_all_books()
        return {"message": "Tüm kitaplar getirildi", "data": books}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")

@router.get("/category/{category_id}")
async def get_books_by_category_endpoint(category_id: int):
    try:
        books = get_books_by_category(category_id)
        return {"message": "Kategoriye göre kitaplar getirildi", "data": books}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")

@router.delete("/delete_book/{books_id}")
async def delete_books_by_id_endpoint(books_id: int):
    try:
        delete_books_by_id(books_id)
        return {"message": f"{books_id} numaralı kitap silindi."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")

@router.put("/update_book")
async def update_books_endpoint(books: UpdateBoosRequest):
    try:
        update_books(
            books_id=books.books_id,
            title=books.title,
            author=books.author,
            description=books.description,
            category_id=books.category_id,
            published_year=books.published_year
        )
        return {"message": "Kitap bilgileri güncellendi"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")

@router.get("/search")
async def search_books_by_keyword_endpoint(keyword: str):
    try:
        books = search_books_by_keyword(keyword)
        return {"message": f"'{keyword}' için arama sonuçları getirildi", "data": books}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")
