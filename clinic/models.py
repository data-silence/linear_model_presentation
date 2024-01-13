from sqlalchemy import Column, Integer, String, BigInteger
from db import Base


class TableDog(Base):
    __tablename__ = "dog"
    __table_args__ = {"schema": "public"}

    pk = Column(Integer, primary_key=True)
    kind = Column(String, nullable=False)
    name = Column(String, nullable=False)


class TableTimeStamp(Base):
    __tablename__ = "timestamp"
    __table_args__ = {"schema": "public"}

    id = Column(BigInteger, primary_key=True)
    timestamp = Column(BigInteger)
