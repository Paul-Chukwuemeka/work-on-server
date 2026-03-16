from lib.database import Base
from sqlalchemy import Column,Integer,String


class User(Base):
    __tablename__ = 'users'
    
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String,nullable=False)
    password=Column(String,nullable=False)
    email=Column(String,nullable=False)
    name=Column(String,nullable=False)
    country=Column(String,nullable=False)