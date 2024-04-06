# Определение класса корневого запроса
import uuid
from typing import List

import strawberry

from app.container import APP_CONTAINER
from app.domain.entities.cart import Cart
from app.domain.entities.product import Product


@strawberry.type
class Query:

    # Метод для получения списка товаров
    @strawberry.field
    def products(self) -> List[Product]:
        """Логика для получения списка товаров"""
        product_adapter = APP_CONTAINER.product_adapter()
        return product_adapter.get_all()

    # Метод для получения списка товаров
    @strawberry.field
    def cart(self, id_: str) -> Cart:
        """Логика для получения корзины товаров по id"""
        pass
