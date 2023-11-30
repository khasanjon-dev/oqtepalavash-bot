"""This package is used for a bot logic implementation."""
from .echo import echo_router
from .help import help_router
from .start import start_router

routers = (start_router, help_router, echo_router)
