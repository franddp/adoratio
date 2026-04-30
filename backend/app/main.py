from fastapi import FastAPI
from app.routers import songs
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Adoratio API "}

app.include_router(songs.router)