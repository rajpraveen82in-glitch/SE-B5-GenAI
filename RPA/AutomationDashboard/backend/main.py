from fastapi import FastAPI
from fastapi.responses import JSONResponse
from backend.selenium_news import fetch_news

app = FastAPI()

@app.get("/news/{keyword}")
def get_news(keyword: str):
    articles = fetch_news(keyword)
    return JSONResponse(content={"keyword": keyword, "articles": articles})
