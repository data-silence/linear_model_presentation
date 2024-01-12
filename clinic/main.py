from fastapi import FastAPI, Depends
from datetime import datetime as dt
from sqlalchemy.orm import Session
from models import TableDog, TableDogType, TableTimeStamp
from schemas import Dog, DogType, Timestamp
from db import SessionLocal

app = FastAPI()


def get_session():
    with SessionLocal() as session:
        return session


@app.get("/", response_model=str)
def root():
    """
    Returns the greeting from the pet clinic
    """
    return 'Welcome to the pet clinic!'


@app.post("/post", response_model=Timestamp)
def get_post(db: Session = Depends(get_session)):
    now = dt.now()
    new_timestamp = TableTimeStamp(id=id(now) // 100,
                                   timestamp=int(round(now.timestamp())) // 100)
    db.add(new_timestamp)
    db.commit()
    db.refresh(new_timestamp)
    return new_timestamp


@app.get("/dog", response_model=list[Dog])
def get_all_dog(limit: int = 100, db: Session = Depends(get_session)):
    return db.query(TableDog).limit(limit).all()  # возвращение запроса на получение данных из базы


@app.post("/dog", response_model=Dog)
def create_dog(dog: Dog, db: Session = Depends(get_session)):
    new_dog = TableDog(pk=dog.pk, name=dog.name, kind=dog.kind)
    db.add(new_dog)
    db.commit()
    db.refresh(new_dog)
    return new_dog  # отработать вариант, когда уже есть такая собака


@app.get("/dog/{pk}", response_model=Dog)
def get_dog_by_id(pk: int, db: Session = Depends(get_session)):
    return db.query(TableDog).filter(TableDog.pk == pk).first()  # отработать вариант, если нет такого id


@app.patch("/dog/{pk}, response_model=Dog")
def update_dog(pk: int, new_dog: Dog):  # подумать, как сделать любое количество изменений
    return {"name": new_dog.name, "pk": pk, "kind": new_dog.kind}
