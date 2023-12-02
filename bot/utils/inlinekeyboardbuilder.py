from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def inline_keyboard_builder(messages: list, sizes: list | None = None):
    builder = InlineKeyboardBuilder()
    for message in messages:
        builder.add(
            InlineKeyboardButton(text=message, callback_data='ok')
        )
    builder.adjust(*sizes)
    return builder.as_markup()
