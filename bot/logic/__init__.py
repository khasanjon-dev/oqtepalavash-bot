"""This package is used for a bot logic implementation."""
from .call_backs import callback_router, order_router
from .menu import menu_router
from .product import product_router
from .register import register_router

routers = (register_router, menu_router, callback_router, order_router, product_router)
