"""Product Repository Adapter SQLALCHEMY"""

# Modules
from src.domain import repositories


class ProductSQLAlchemyRepository(repositories.ProductAbstractRepository):
    def __init__(self, session: Session):
        super().__init__(session)

    def _add(self, new_element: models.ItemRepository) -> models.ItemRepository:
        return self.session.add(new_element)
