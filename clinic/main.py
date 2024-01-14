from fastapi import FastAPI, Depends, HTTPException
from datetime import datetime as dt
from sqlalchemy.orm import Session
from models import TableDog, TableTimeStamp, Base
from schemas import Dog, DogType, Timestamp
from db import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_session() -> None:
    """Manages connection sessions for working with the database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=str)
def root():
    """Returns the greeting from the pet clinic"""
    return 'Welcome to our pet clinic!'


@app.post("/post", response_model=Timestamp)
def get_post(db: Session = Depends(get_session)):
    """Fixing id and timestamp for new dog"""
    now = dt.now()
    new_timestamp = TableTimeStamp(id=id(now) // 100,
                                   timestamp=int(round(now.timestamp())) // 100)
    db.add(new_timestamp)
    db.commit()
    db.refresh(new_timestamp)
    return new_timestamp


@app.get("/dog", response_model=list[Dog])
def get_dogs(limit: int = 100, db: Session = Depends(get_session)):
    """Get all registered dogs in clinic"""
    return db.query(TableDog).limit(limit).all()


@app.post("/dog", response_model=Dog)
def create_dog(dog: Dog, db: Session = Depends(get_session)):
    """Registration the dog in clinic"""
    db_dog = get_dog_by_pk(pk=dog.pk)
    if db_dog:
        raise HTTPException(status_code=400, detail="Эта собака уже записана в нашу базу данных")
    new_dog = TableDog(pk=dog.pk, name=dog.name, kind=dog.kind)
    db.add(new_dog)
    db.commit()
    db.refresh(new_dog)
    return new_dog


@app.get("/dog/{pk}", response_model=Dog)
def get_dog_by_pk(pk: int, db: Session = Depends(get_session)):
    """Find the dog in clinic by id"""
    db_dog = db.query(TableDog).filter(TableDog.pk == pk).first()
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Такая собака не найдена")
    return db_dog


@app.get("/dog_kind/{kind}", response_model=list[Dog])
def get_dog_by_kind(kind: DogType, db: Session = Depends(get_session)):
    """Find all the dogs of a particular type"""
    db_dogs = db.query(TableDog).filter(TableDog.kind == kind.value).all()
    if db_dogs is None:
        raise HTTPException(status_code=404, detail=f"Собак пароды {kind} у нас нет")
    return db_dogs


@app.patch("/dog/{pk}", response_model=Dog)
def update_dog(pk: int, dog: Dog, db: Session = Depends(get_session)):
    """Updates information about the selected dog by id"""
    updated_dog = db.query(TableDog).get(pk)
    if updated_dog:
        updated_dog.kind = dog.kind
        updated_dog.name = dog.name
        db.add(updated_dog)
        db.commit()
        db.refresh(updated_dog)
    else:
        raise HTTPException(status_code=404, detail=f"Cобака за номером {pk} не найдена")

    return updated_dog
