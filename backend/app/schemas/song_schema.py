from pydantic import BaseModel

class SongCreate (BaseModel):
    title: str
    key: str