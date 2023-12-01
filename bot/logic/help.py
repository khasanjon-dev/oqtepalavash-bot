"""This file represents a start logic."""

from aiogram import Router, types
from aiogram.filters import Command

help_router = Router(name='help')


@help_router.message(Command(commands='help'))
async def help_handler(message: types.Message) -> None:
    """Help command handler."""
    await message.answer('Hi, world!')
