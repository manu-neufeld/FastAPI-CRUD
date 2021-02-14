
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime


Base = declarative_base()

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    body = Column(Text)
    is_published = Column(Boolean)
    created = Column(DateTime, default=datetime.utcnow().strftime("%Y-%m-%d" "%H:%M:%S"))
    modified = Column(DateTime, default=datetime.utcnow().strftime("%Y-%m-%d" "%H:%M:%S"))
