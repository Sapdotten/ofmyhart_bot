from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text, Engine
import asyncio
from database.db_settings import DBSettings
import logging

engine: Engine


def init_engine():
    global engine
    engine = create_async_engine(url=DBSettings.get_url(), max_overflow=10, echo=True)
    logging.info("Engine for database is initialized")
    return engine
