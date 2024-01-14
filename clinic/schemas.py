from enum import Enum
from pydantic import BaseModel


class DogType(str, Enum):
    """"Enum Class, contains the available dog species"""
    TERRIER = 'terrier'
    BULLDOG = 'bulldog'
    DALMATIAN = "dalmatian"


class Dog(BaseModel):
    """Dog table data schema for Pydantic model"""
    pk: int
    kind: DogType
    name: str


class Timestamp(BaseModel):
    """Timestamp data schema for Pydantic model"""
    id: int
    timestamp: int
