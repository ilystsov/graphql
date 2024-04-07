from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from app.infrastructure.adapter.cart import CartAdapter
from app.infrastructure.adapter.product import ProductAdapter
from app.settings.app import AppSettings


class AppContainer(DeclarativeContainer):
    app_settings: Singleton["AppSettings"] = Singleton(AppSettings)
    product_adapter: Singleton["ProductAdapter"] = Singleton(ProductAdapter) # везде должны использовать один адаптер, чтобы было персистентное хранилище
    cart_adapter: Singleton["CartAdapter"] = Singleton(CartAdapter)

APP_CONTAINER = AppContainer()
