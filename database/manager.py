from database.models import Users, Base
from database.connect_db import init_engine
from sqlalchemy import MetaData, text
import asyncio
import logging

engine = init_engine()
async def init_models():
    async with engine.begin() as conn:
        is_exist = await conn.execute(text("select exists(select 1 from information_schema.tables where table_name='users')"))
        if is_exist.fetchone():
            logging.info("Db already exists")
        else:
            logging("Creating db...")
            await conn.run_sync(Base.metadata.create_all)
asyncio.run(init_models())

