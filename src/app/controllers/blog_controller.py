from sqlalchemy.orm import Session

from src.app.models.blog import Blog
from src.app.schemas.blog import BlogCreate
from fastapi import HTTPException
from fastapi import HTTPException
from src.app.models.blog import Blog
from fastapi import HTTPException
from fastapi import HTTPException

def delete_blog(db, id):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    db.delete(blog)
    db.commit()

    return {"message": "Blog deleted successfully"}

def update_blog(db, id, blog):
    old_blog = db.query(Blog).filter(Blog.id == id).first()

    if not old_blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    old_blog.title = blog.title
    old_blog.content = blog.content

    db.commit()
    db.refresh(old_blog)

    return old_blog

def get_blog(db, id):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    return blog

def get_blog_by_id(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    return blog

def get_all_blogs(db: Session):
    return db.query(Blog).all()


def create_blog(db: Session, blog: BlogCreate):
    new_blog = Blog(
        title=blog.title,
        content=blog.content
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog