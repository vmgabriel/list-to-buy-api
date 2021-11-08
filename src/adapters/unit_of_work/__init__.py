"""Unit of Work"""

# Config
from src.config import config, ORMMOdule

# Modules
from . import sqlalquemy
from src.domain.unit_of_work import AbstractUnitOfWork


unit_of_work: AbstractUnitOfWork = None


if config.ORM_MODULE == ORMMOdule.SQLALCHEMY:
    unit_of_work = sqlalquemy.SqlAlchemyUnitOfWork
