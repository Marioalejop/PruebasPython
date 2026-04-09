from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Libro(Base):
    __tablename__ = 'libros'
    id         = Column(Integer, primary_key=True)
    titulo     = Column(String, nullable=False)
    autor      = Column(String, nullable=False)
    disponible = Column(Boolean, default=True)
