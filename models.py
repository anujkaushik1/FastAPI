from sqlalchemy import Column, Integer, String
from database import Base

#Database Table

class Item(Base):     #Item iherit from Base
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
