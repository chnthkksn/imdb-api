from typing import Union
from fastapi import FastAPI
import uvicorn

from src.search import search
from src.getData import getData
from src.getImages import getImages
from src.getakas import getAkas

app = FastAPI(
    title="IMDB Unofficial API",
    description= "API to get info and images from IMDB movies",
    version="0.0.1",
    contact={
        "name": "Chinthaka Kasun",
        "url": "http://www.itschinth.tk",
        "email": "chnthkksn@gmail.com"
    })


@app.get("/", tags=["Status"])
async def read_root():
    return {"Working": "Go to /docs for more info"}


@app.get("/api/getinfo/{movie_id}", tags=["IMDB"])
async def read_item(movie_id: str):
    return getData(movie_id)


@app.get("/api/getimg/{movie_id}", tags=["IMDB"])
async def read_item(movie_id: str, limit: Union[int, None] = None):
    return getImages(movie_id, limit)

@app.get("/api/search/{q}", tags=["IMDB"])
async def read_item(q: str):
    return search(q)

@app.get('/api/akas/{movie_id}', tags=["IMDB"])
async def read_item(movie_id: str):
    return getAkas(movie_id)    

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=1)