"""This file represents a start logic."""

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.data.data import language
from bot.requests.users import get_user_or_create
from bot.utils.keyboardbuilder import keyboard_builder
from bot.utils.states import states

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext) -> None:
    user = await get_user_or_create(message.from_user.id)
    await state.set_state(states.language)
    reply_markup = await keyboard_builder(language.values(), [1])
    user = message.from_user
    first_message = (f"Assalomu alaykum {user.first_name}. Men Oqtepa Lavash yetkazib berish xizmati botiman!\n"
                     f"Привет {user.first_name}! Я бот службы доставки Oqtepa Lavash!\n"
                     f"Hi {user.first_name}! I am Oqtepa Lavash delivery service bot!")
    second_message = (
        "Muloqot tilini tanlang\n"
        "Выберите язык\n"
        "Select Language"
    )
    await message.answer(first_message)
    await message.answer(second_message, reply_markup=reply_markup)
