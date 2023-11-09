from pydantic import BaseModel


class MusicBase(BaseModel):
    genre: str
    song_name: str
    title: str
    artist: str
    isDisabled: bool
