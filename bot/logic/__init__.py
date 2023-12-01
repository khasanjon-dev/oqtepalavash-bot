"""This package is used for a bot logic implementation."""
from .echo import echo_router
from .help import help_router
from .start import router

routers = (router, help_router, echo_router)
