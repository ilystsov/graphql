import uuid
from typing import Dict

from app.domain.entities.cart import Cart
from app.domain.entities.product import ProductQuantity
from app.domain.services.interfaces.cart import CartInterface
from app.infrastructure.adapter.exceptions import CartNotFound, ProductNotFound


class CartAdapter(CartInterface):
    """
    Адаптер для работы с корзинами продуктов.
    """

    _carts: Dict[str, Cart]

    def __init__(self):
        self._carts = {}

    def create(self) -> "Cart":
        cart = Cart(id=str(uuid.uuid4()), products=[])
        self._carts[cart.id] = cart
        return cart

    def delete(self, cart_id: str) -> "Cart":
        if cart_id not in self._carts:
            raise CartNotFound('There is no cart with the specified id.')
        return self._carts.pop(cart_id)

    def add_product(self, cart_id: str, product_id: str) -> "Cart":
        from app.container import APP_CONTAINER     # избегаем циклических зависимостей
        if cart_id not in self._carts:
            raise CartNotFound('There is no cart with the specified id.')
        cart = self._carts[cart_id]
        for product_quantity in cart.products:
            if product_quantity.product.id == product_id:
                product_quantity.quantity += 1
                break
        else:
            product_adapter = APP_CONTAINER.product_adapter()
            try:
                new_product = product_adapter.get_product_by_id(product_id)
            except ProductNotFound:
                raise
            new_product_quantity = ProductQuantity(product=new_product, quantity=1)
            cart.products.append(new_product_quantity)
        return cart

    def change_product_quantity(self, cart_id: str, product_id: str, quantity: int) -> "Cart":
        if cart_id not in self._carts:
            raise CartNotFound('There is no cart with the specified id.')
        cart = self._carts[cart_id]
        for product_quantity in cart.products:
            if product_quantity.product.id == product_id:
                product_quantity.quantity = quantity
                return cart

        raise ProductNotFound('There is no product in the cart with the specified id.')

    def get_cart_by_id(self, cart_id: str) -> "Cart":
        if cart_id not in self._carts:
            raise CartNotFound('There is no cart with the specified id.')
        return self._carts[cart_id]
