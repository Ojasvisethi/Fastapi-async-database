from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    url="sqlite+aiosqlite:///./fastapi-prac3.db",
    echo=True
)

class Base(DeclarativeBase):
    pass

async def get_db():
    db = AsyncSession(engine)
    try:
        yield db
    finally:
        await db.close()