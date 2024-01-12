from datetime import datetime as dt
from enum import Enum
from pydantic import BaseModel
# from typing import Union, Optional


class DogType(Enum):
    TERRIER: str = 'terrier'
    BULLDOG: str = 'bulldog'
    DALMATIAN: str = "dalmatian"


class Dog(BaseModel):
    pk: int
    kind: DogType
    name: str


class Timestamp(BaseModel):
    id: int
    timestamp: int