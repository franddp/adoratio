from fastapi import APIRouter
from app.schemas.song_schema import SongCreate

router = APIRouter()

@router.get("/songs")
def get_songs():
    return [
        {
            "title": "Hossanna",
            "key": "C"        
        },
        {
            "title": "Oceans",
            "key": "F"
        }
    ]

@router.post("/songs")
def create_song(song : SongCreate):
    return {
        "message": "Song created",
        "song": song
    }