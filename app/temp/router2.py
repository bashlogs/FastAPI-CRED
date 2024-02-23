from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from schemas import RequestBook, Response
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
async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
    created_book = crud.create_book(db, book=request.parameter)
    return Response(status_code=200, content={"message": "Book created successfully", "result": created_book})

@router.get("/")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip, limit)
    return Response(status="Ok", code=200, message="Success fetch all data", result=books)

@router.patch("/update")
async def update_book(request: RequestBook, db: Session = Depends(get_db)):
    updated_book = crud.update_book(db, book_id=request.parameter.id,
                                    title=request.parameter.title,
                                    description=request.parameter.description)
    return Response(status="Ok", code=200, message="Success update data", result=updated_book)

@router.delete("/delete")
async def delete_book(request: RequestBook, db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=request.parameter.id)
    return Response(status="Ok", code=200, message="Success delete data")
