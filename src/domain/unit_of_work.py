"""Unit Of Work Pattern - Abstract Definitio"""

# Libraries
from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod

# Modules
from . import repositories


class AbstractUnitOfWork(ABC):
    products: repositories.ProductAbstractRepository
    lists: repositories.ListAbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        event_repositories: List[repositories.all_repositories] = []
        for repository in event_repositories:
            for event_model in self.event_models.seen:
                while event_model.events:
                    yield event_model.events.pop(0)

    @abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError
