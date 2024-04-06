# Определение класса товара
from typing import Optional

import strawberry


@strawberry.type
class Product:
    id: str
    name: str
    price: float = 0.


@strawberry.input
class ProductInput:
    name: str
    price: Optional[float] = None


@strawberry.type
class ProductQuantity:
    product: Product
    quantity: int
