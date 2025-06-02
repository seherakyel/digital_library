from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models.comments import (
    add_comments,get_comments_by_book_id,delete_comment,get_comment_count_for_book
)

router = APIRouter()

class AddCommentRequest(BaseModel):
    user_id: int
    book_id: int
    content: str

class DeleteCommentRequest(BaseModel):
    comment_id: int

@router.post("/add_comment")
async def add_comment_endpoint(comment: AddCommentRequest):
    try:
        add_comments(comment.user_id, comment.book_id, comment.content)
        return JSONResponse(content={"message": "Yorum başarıyla eklendi."})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")

@router.get("/comments/{book_id}")
async def get_comments_by_book_id_endpoint(book_id: int):
    try:
        comments = get_comments_by_book_id(book_id)
        return {"message": "Yorumlar getirildi", "data": comments}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")

@router.delete("/delete_comment")
async def delete_comment_endpoint(request: DeleteCommentRequest):
    try:
        delete_comment(request.comment_id)
        return {"message": f"{request.comment_id} numaralı yorum başarıyla silindi."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")

@router.get("/comment_count/{book_id}")
async def get_comment_count_for_book_endpoint(book_id: int):
    try:
        count = get_comment_count_for_book(book_id)
        return {"message": f"Kitap {book_id} için toplam yorum sayısı", "count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hata: {str(e)}")