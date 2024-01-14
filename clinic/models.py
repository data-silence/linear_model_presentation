from sqlalchemy import Column, Integer, String, BigInteger
from db import Base


class TableDog(Base):
    """Model for working with the table dog"""
    __tablename__ = "dog"
    __table_args__ = {"schema": "public"}
    # Наверное, тут должен был быть внешний ключ, связанный с полем id таблицы TimeStamp,
    # который бы генерировался одновременно при создании собаки, и присваивался создаваемой собаке
    # с учетом отсутствии описания взаимосвязи таблиц в задании и возможным недопониманием + нераскрытием тем миграций,
    # я не стал усложнять себе жизнь и реализовывать возможно неправильное своё понимание.
    pk = Column(Integer, primary_key=True)
    kind = Column(String, nullable=False)
    name = Column(String, nullable=False)


class TableTimeStamp(Base):
    """Model for working with the table timestamp"""
    __tablename__ = "timestamp"
    __table_args__ = {"schema": "public"}

    id = Column(BigInteger, primary_key=True)
    timestamp = Column(BigInteger)
