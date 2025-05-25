
import sys
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from models.users import (
    get_users_full_info_by_id,get_users_by_user_name,delete_users_by_id,update_users,is_active, Users_login,Register_users
)

router = APIRouter()

class RegisterUser(BaseModel):
    user_name: str
    email:str
    password:str


class UpdateUsers(BaseModel):
    users_id:int
    user_name: Optional[str]
    email:Optional[str]
    password:Optional[str]
    is_active:Optional[int]

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login_endpoint(request: LoginRequest):
    users = Users_login(request.email, request.password)
    if users:
        email = users.get('email', 'Bilinmiyor')
        return JSONResponse(content={
            "message": f"giris basarili: Hoş geldin {email}",
            "users": users
        })
    else:
        raise HTTPException(status_code=401, detail="kullanici email veya şifre hatali.")
    


@router.post("/register")
async def Register_users_endpoint(users: RegisterUser):
    result = Register_users(users.user_name, users.email, users.password,)
    if result:
        return JSONResponse(content={"message": f"{users.user_name} başarıyla kayıt oldu."})
    else:
        raise HTTPException(status_code=400, detail="Kayıt işlemi başarısız. Kullanıcı adı alınmış olabilir.")




@router.get("/user/{user_name}")
async def get_users_by_user_name(user_name: str):
    try:
        user = get_users_by_user_name(user_name)
        if user:
            return {"message": "User found", "user": user, "status": 200}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="kullanici getirelemedi")



@router.delete("/delete/{users_id}")
async def delete_users_by_id_enpoint(users_id: int):
    try:
        delete_users_by_id(users_id)
        return {"message": "User deleted"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="kullanici silinmedi.")
    


@router.get("/is_active/{users_id}")
async def is_active_endpoint(users_id: int):
    try:
        is_active(users_id)
        return {"message": "aktif durumu kontrol edildi"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")



@router.get("/get_users/{users_id}")
async def get_users_full_info_by_id_endpoint(users_id: int):
    try:
        user = get_users_full_info_by_id(users_id)
        if user:
            return {"message": "Kullanıcı bulundu", "data": user}
        else:
            return {"message": "Kullanıcı bulunamadı", "data": None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")
    


@router.put("/update_users") # PUT isteği: Var olan kullanıcıyı güncellemek için kullanılır
async def update_users_endpoint(users: UpdateUsers): # Gelen veri, UpdateUser modeline göre kontrol edilir
    try:
        update_users(
            users_id=users.users_id, # Gelen veri, UpdateUser modeline göre kontrol edilir
            user_name=users.user_name, # Yeni ad (gönderildiyse)
            email=users.email,
            password=users.password,
            is_active=users.is_active # aktiflik durumu (1 veya 0)
        )
        return {"message": "Kullanıcı güncellendi"} # İşlem başarılıysa bu mesaj dönülür
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")



