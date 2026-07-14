from pydantic import BaseModel


class BlogCreate(BaseModel):
    title: str
    content: str


class BlogResponse(BlogCreate):
    id: int

    class Config:
        from_attributes = True