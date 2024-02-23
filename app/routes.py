from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import BookSchema
import crud
from config import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create_book_service(request: BookSchema, db: Session = Depends(get_db)):
    created_book = crud.create_book(db, book=request)
    return {"message": "Book created successfully", "result": created_book}

@router.get("/")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip, limit)
    return {"message": "Success fetch all data", "result": books}

@router.get("/{book_id}")
async def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if book:
        return {"message": "Success fetch book by id", "result": book}
    return {"message": "Book not found", "result": None}

@router.patch("/update")
async def update_book(request: BookSchema, db: Session = Depends(get_db)):
    updated_book = crud.update_book(db, book_id=request.id,
                                    title=request.title,
                                    description=request.description)
    return {"message": "Success update data", "result": updated_book}

@router.delete("/delete")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=book_id)
    return {"message": "Success delete data"}
