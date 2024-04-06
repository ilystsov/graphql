from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from app.infrastracture.adapter.product import ProductAdapter
from app.settings.app import AppSettings


class AppContainer(DeclarativeContainer):
    app_settings: Singleton["AppSettings"] = Singleton(AppSettings)
    product_adapter: Singleton["ProductAdapter"] = Singleton(ProductAdapter)


APP_CONTAINER = AppContainer()
