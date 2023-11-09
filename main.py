from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
import pandas as pd
from db import get_db
from models import Music
from schema import MusicBase

app = FastAPI()


def read_and_insert_data(filename, nrows=5, chunk_size=1):
    for i, chunk in enumerate(pd.read_csv(filename, nrows=nrows, chunksize=chunk_size)):
        for row_dict in chunk.to_dict(orient="records"):
            yield row_dict


@app.post('/create_music')
async def create_music(db: AsyncSession = Depends(get_db)):
    # Create a new Music model instance
    csv_file_path = r'C:\audio.musics123.csv'
    new_music_list = []

    for data_chunk in read_and_insert_data(csv_file_path, nrows=5, chunk_size=1):
        new_music = Music(
            genre=data_chunk['genre'],
            songname=data_chunk['songname'],
            title=data_chunk['title'],
            artist=data_chunk['artist'],
            isDisabled=data_chunk['isDisabled'])

        new_music_list.append(new_music)

    db.add_all(new_music_list)
    await db.commit()

    for new_music in new_music_list:
        await db.refresh(new_music)

    return {"message": "Music entries created successfully"}
