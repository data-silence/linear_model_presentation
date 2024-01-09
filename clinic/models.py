from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship
from db import Base, SessionLocal


class TableDog(Base):
    __tablename__ = "dog"
    __table_args__ = {"schema": "public"}

    pk = Column(Integer, primary_key=True)
    kind = Column(String)
    name = Column(String)


class TableDogType(Base):
    __tablename__ = "dog_type"
    __table_args__ = {"schema": "public"}
    kind = Column(String, primary_key=True)

class TableTimeStamp(Base):
    __tablename__ = "timestamp"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer)
