from enum import Enum

from aiogram.filters.callback_data import CallbackData


class MainMenu(str, Enum):
    menu = 'menu'
    about = 'about'
    orders = 'orders'
    states = 'states'
    write = 'write'
    settings = 'settings'
    new_order = 'new_order'


class MainMenuCallBack(CallbackData, prefix='main_menu'):
    choice: MainMenu


class Menu(str, Enum):
    order = 'order'
    about = 'about'
    orders = 'orders'
    states = 'states'
    write = 'write'
    settings = 'settings'


class MenuCallBack(CallbackData, prefix='menu'):
    choice: Menu
