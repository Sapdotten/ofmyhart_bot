from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    __tableargs__ = {'comment': "Таблица с пользователями бота"}
    
    user_id = Column(
        Integer,
        nullable = False,
        unique = True,
        primary_key = True,
        autoincrement=False
    )
    name = Column(String(128), comment = 'Имя юзера из telegram')