import sys
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from models.categories import (  
delete_categories_by_id,get_all_categories,get_categories_by_id,add_categories)

router = APIRouter()

# Tüm kategorileri getir
@router.get("/categories")
def read_all_categories():
    result = get_all_categories()
    if result is None:
        raise HTTPException(status_code=500, detail="Kategoriler listelenemedi")
    return {"categories": result}

# ID'ye göre kategori getir
@router.get("/categories/{category_id}")
def read_category_by_id(category_id: int):
    result = get_categories_by_id(category_id)
    if result is None or len(result) == 0:
        raise HTTPException(status_code=404, detail=f"{category_id} id'li kategori bulunamadı")
    return {"category": result}

# Yeni kategori ekle
@router.post("/categories")
def create_category(name: str):
    result = add_categories(name)
    if result is None:
        raise HTTPException(status_code=500, detail="Kategori eklenemedi")
    return {"message": f"{name} başarıyla eklendi"}

# ID'ye göre kategori sil
@router.delete("/categories/{category_id}")
def delete_category(category_id: int):
    result = delete_categories_by_id(category_id)
    if result is None:
        raise HTTPException(status_code=500, detail="Kategori silinemedi")
    return {"message": f"{category_id} id'li kategori başarıyla silindi"}