from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth import verify_token

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Mevcut kullanıcıyı token'dan al"""
    token = credentials.credentials
    user_id = verify_token(token)
    return user_id

def get_current_admin_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Admin kullanıcı kontrolü"""
    token = credentials.credentials
    user_id = verify_token(token)
    
    # Burada veritabanından kullanıcının admin olup olmadığını kontrol etmeniz gerekir
    # Şimdilik basit bir örnek:
    if user_id != "admin":  # Gerçek projede veritabanından kontrol edin
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return user_id