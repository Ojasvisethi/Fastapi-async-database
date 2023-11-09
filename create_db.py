from sqlalchemy import inspect

from db import Base,engine
import asyncio

async def create_db():
    async with engine.begin() as conn:
        from models import Music

        inspector = inspect(conn)

        # Check if the 'Music' table exists in the database
        if 'Music' not in inspector.get_table_names():
            # If the table doesn't exist, create it
            await conn.run_sync(Base.metadata.create_all)

        await engine.dispose()


asyncio.run(create_db())