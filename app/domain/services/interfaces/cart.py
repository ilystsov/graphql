from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING


if TYPE_CHECKING:
    from app.domain.entities.cart import Cart


class CartInterface(Protocol):
    """Интерфейс для работы с корзиной."""

    @abstractmethod
    def create(self) -> "Cart":
        """Создать корзину."""

    @abstractmethod
    def delete(self, product_id: str) -> "Cart":
        """Удалить корзину."""

    @abstractmethod
    def add_product(self, product_id: str) -> "Cart":
        """Добавить продукт корзину."""

    @abstractmethod
    def change_product_quantity(self, product_id: str, quantity: int) -> "Cart":
        """Изменить кол-во товаров в корзине."""

