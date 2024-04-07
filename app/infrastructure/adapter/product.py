import uuid
from typing import List, Dict

from app.domain.services.interfaces.product import ProductInterface
from app.domain.entities.product import Product
from app.infrastructure.adapter.exceptions import ProductNotFound


class ProductAdapter(ProductInterface):
    """
    Адаптер для работы с продуктами.
    """

    _products: Dict[str, Product]

    def __init__(self):
        self._products = {}

    def create(self, name: str, price: float) -> Product:
        """Создать продукт."""
        product = Product(id=str(uuid.uuid4()), name=name, price=price)
        self._products[product.id] = product
        return product

    def delete(self, id_: str) -> Product:
        """Удалить продукт."""
        if id_ not in self._products:
            raise ProductNotFound('There is no product with the specified id.')
        return self._products.pop(id_)

    def get_all(self) -> List[Product]:
        """Получить все доступные продукты."""
        return list(self._products.values())

    def update_name(self, id_: str, name: str) -> "Product":
        """Обновить имя продукта."""
        if id_ not in self._products:
            raise ProductNotFound('There is no product with the specified id.')
        self._products[id_].name = name
        return self._products[id_]

    def update_price(self, id_: str, price: float) -> Product:
        """Обновить цену продукта."""
        if id_ not in self._products:
            raise ProductNotFound('There is no product with the specified id.')
        self._products[id_].price = price
        return self._products[id_]

    def get_product_by_id(self, id_: str) -> "Product":
        if id_ not in self._products:
            raise ProductNotFound('There is no product with the specified id.')
        return self._products[id_]