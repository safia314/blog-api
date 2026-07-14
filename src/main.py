from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.app.database import Base, engine
from src.app.models.blog import Blog
from src.app.routes.blog import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
def home():

    with open("src/templates/index.html") as file:
        return file.read()