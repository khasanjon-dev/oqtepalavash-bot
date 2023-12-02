from enum import Enum

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Menu(str, Enum):
    order = 'order'
    about = 'about'
    orders = 'orders'
    states = 'states'
    write = 'write'
    settings = 'settings'


class MenuCallBack(CallbackData, prefix="menu"):
    choice: Menu


def inline_keyboard_builder(messages: list[str], call_backs: list[str], sizes: list | None = None):
    builder = InlineKeyboardBuilder()
    for i in range(len(messages)):
        builder.add(
            InlineKeyboardButton(
                text=messages[i],
                callback_data=MenuCallBack(choice=call_backs[i]).pack()
            )
        )
    builder.adjust(*sizes)
    return builder.as_markup()
