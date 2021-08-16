rom datetime import datetime

from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
