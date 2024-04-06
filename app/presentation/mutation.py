# Определение класса корневой мутации
import uuid
from typing import Optional, TYPE_CHECKING

import strawberry

from app.container import APP_CONTAINER
from app.domain.entities.cart import Cart
from app.domain.entities.product import Product, ProductInput
from app.infrastracture.adapter.product import ProductAdapter


@strawberry.type
class Mutation:

    # Метод для создания продукта
    @strawberry.mutation
    def create_product(self, product_info: ProductInput) -> Product:
        """Логика создания продукта"""
        product_adapter = APP_CONTAINER.product_adapter()
        return product_adapter.create(name=product_info.name,
                                      price=float(product_info.price) if product_info.price else 0)

    @strawberry.mutation
    def update_product_info(self, id_: str, product_info: ProductInput) -> Product:
        """Обновить данные о продукте."""
        pass

    @strawberry.mutation
    def create_cart(self) -> Cart:
        """Логика создания корзины"""
        pass

    @strawberry.mutation
    def add_to_cart(self, cart_id: str, product_name: str, quantity: int) -> str:
        """Метод добавления товара в корзину"""
        pass
