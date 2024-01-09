from fastapi import FastAPI, Depends
from datetime import datetime as dt
from sqlalchemy.orm import Session
from models import TableDog, TableDogType, TableTimeStamp
from schemas import Dog, DogType, Timestamp
from db import SessionLocal

# class DogType(str, Enum):
#     TERRIER = 'terrier'
#     BULLDOG = 'bulldog'
#     DALMATIAN = "dalmatian"
#
#
# class Dog(BaseModel):
#     pk: int
#     kind = DogType
#     name: str
#
#
# class Timestamp(BaseModel):
#     id: int
#     timestamp: int


app = FastAPI()


def get_session():
    with SessionLocal() as session:
        return session


@app.get("/")
def root() -> str:
    """
    Returns the greeting from the pet clinic
    """
    return 'Welcome to the pet clinic!'


@app.post("/post")
def get_post() -> Timestamp:
    now = dt.now()
    new_timestamp = Timestamp(id=id(now),
                              timestamp=int(round(now.timestamp())))
    return new_timestamp  # возвращение запроса на запись в базу


@app.get("/dog", response_model=list[Dog])
def get_all_dog(limit=10, db: Session = Depends(get_session)):
    return db.query(TableDog).limit(limit).all()  # возвращение запроса на получение данных из базы
#
#
# @app.post("/dog")
# def create_dog(dog: Dog):
#     return {"name": dog.name, "pk": dog.pk, "kind": dog.kind}
#
#
# @app.get("/dog/{pk}", response_model=Dog)
# def get_dog_by_id(pk: int):
#     return {"name": 'string', "pk": 0, "kind": DogType.TERRIER}  # возвращение запроса на получение данных из базы
#
#
# @app.patch("/dog/{pk}, response_model=list[Dog]")
# def update_dog(pk: int, new_dog: Dog):
#     return {"name": new_dog.name, "pk": pk, "kind": new_dog.kind}
