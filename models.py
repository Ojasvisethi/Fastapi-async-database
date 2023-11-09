from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db import Base
from sqlalchemy import Column


class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer, primary_key=True, index=True)
    genre = Column(String)
    songname = Column(String)
    title = Column(String)
    artist = Column(String)
    isDisabled = Column(Boolean)
