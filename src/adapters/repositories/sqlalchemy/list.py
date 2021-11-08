"""List Repository Adapter SQLALCHEMY"""

# Modules
from src.domain import repositories


class ListSQLAlchemyRepository(repositories.ListAbstractRepository):
    def __init__(self, session: Session):
        super().__init__(session)
