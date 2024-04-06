import uuid
from typing import List, Optional, Dict

from app.domain.services.interfaces.product import ProductInterface
from app.domain.entities.product import Product


class ProductAdapter(ProductInterface):
    """Адаптер для работы с продуктами."""

    _products: Dict[str, Product]

    def __init__(self):
        self._products = {}

    def create(self, name: str, price: float) -> Product:
        """Создать продукт."""
        product = Product(id=uuid.uuid4(), name=name, price=price)
        self._products[product.id] = product

        print(self._products)

        return product

    def delete(self, id_: str) -> Product:
        """Удалить продукт."""
        # TODO
        pass

    def get_all(self) -> List[Product]:
        """Получить все доступные продукты."""
        return list(self._products.values())

    def update_name(self, id_: str, name: str) -> "Product":
        """Обновить имя продукта."""

    def update_price(self, id_: str, price: float) -> Product:
        """Обновить цену продукта."""
        # TODO
        pass
