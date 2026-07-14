from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.app.controllers.blog_controller import get_all_blogs, create_blog, get_blog
from src.app.database import get_db
from src.app.schemas.blog import BlogCreate
from src.app.controllers.blog_controller import get_all_blogs, create_blog
from src.app.controllers.blog_controller import (
    get_all_blogs,
    create_blog,
    get_blog_by_id
)
router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)
from src.app.controllers.blog_controller import (
    get_all_blogs,
    create_blog,
    get_blog,
    update_blog
)
from src.app.controllers.blog_controller import (
    get_all_blogs,
    get_blog,
    create_blog,
    update_blog,
    delete_blog
)
@router.get("/")
def get_blogs(db: Session = Depends(get_db)):
    return get_all_blogs(db)

@router.post("/")
def add_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    return create_blog(db, blog)


@router.get("/{id}")
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    return get_blog(db, id)

@router.put("/{id}")
def edit_blog(id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    return update_blog(db, id, blog)

@router.delete("/{id}")
def remove_blog(id: int, db: Session = Depends(get_db)):
    return delete_blog(db, id)