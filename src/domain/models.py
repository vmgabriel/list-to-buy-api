"""All Models of Domain"""

# Libraries
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


# Modules
from .events import Event


class Item(BaseModel):
    name: str
    description: str
    quantity: int
    valid: bool
    events: List[Event] = []


class ItemRepository(Item):
    id: Optional[int]
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
    list_id: int


class List(BaseModel):
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
    events: List[Event] = []


class ListRepository(List):
    id: Optional[int]

