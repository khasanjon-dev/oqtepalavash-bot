"""This file represents a start logic."""

from aiogram import Router, types
from aiogram.filters import CommandStart

from bot.data import start_message

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start_handler(message: types.Message):
    """Start command handler."""
    return await message.answer(start_message)
