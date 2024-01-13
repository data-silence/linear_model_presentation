from enum import Enum
from pydantic import BaseModel

class DogType(str, Enum):
    TERRIER = 'terrier'
    BULLDOG = 'bulldog'
    DALMATIAN = "dalmatian"


class Dog(BaseModel):
    pk: int
    kind: DogType
    name: str


class Timestamp(BaseModel):
    id: int
    timestamp: int
