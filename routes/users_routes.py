
import sys
from fastapi import APIRouter, HTTPException, Depends, status
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

# Eski login endpoint'i kaldırıldı - yeni JWT sistemi kullanılıyor
    


# Eski register endpoint'i kaldırıldı - yeni JWT sistemi kullanılıyor




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



# Dosyanın başına ekleyin:
from auth import get_password_hash, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from middleware import get_current_user, get_current_admin_user
from fastapi import status

# Login endpoint'ini güncelleyin:
@router.post("/login")
async def login_endpoint(request: LoginRequest):
    from models.users import authenticate_user
    
    user = authenticate_user(request.email, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user["id"])}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user["id"],
            "user_name": user["user_name"],
            "email": user["email"]
        }
    }

# Register endpoint'ini güncelleyin:
@router.post("/register")
async def register_users_endpoint(users: RegisterUser):
    # Şifreyi hashle
    hashed_password = get_password_hash(users.password)
    
    result = Register_users(users.user_name, users.email, hashed_password)
    if result:
        return JSONResponse(content={"message": f"{users.user_name} başarıyla kayıt oldu."})
    else:
        raise HTTPException(status_code=400, detail="Kayıt işlemi başarısız.")

# Yeni endpoint - Mevcut kullanıcı bilgilerini getir
@router.get("/me")
async def get_current_user_info(current_user: str = Depends(get_current_user)):
    from models.users import get_users_full_info_by_id
    user = get_users_full_info_by_id(int(current_user))
    if user:
        return {"user": user}
    else:
        raise HTTPException(status_code=404, detail="User not found")