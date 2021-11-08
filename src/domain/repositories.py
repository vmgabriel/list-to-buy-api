"""All Abstract Repositories"""

# Libraries
from typing import Union
from abc import ABC, abstractmethod
from pydantic import BaseModel

# Modules
from . import models


class ProductAbstractRepository(ABC):
    def __init__(self, session):
        self.session = session
        self.seen = set()

    def add(self, new_element: models.Item, list_id: int) -> models.ItemRepository:
        item_to_save = models.ItemRepository(**new_element.__dict__, list_id=list_id)
        n_element = _add(item_to_save)
        self.seen.add(n_element)
        return n_element

    @abstractmethod
    def _add(self, new_element: models.ItemRepository) -> models.ItemRepository:
        raise NotImplementedError


class ListAbstractRepository(ABC):
    def __init__(self, session):
        self.session = session
        self.seen = set()


all_repositories = Union[ProductAbstractRepository, ListAbstractRepository]
