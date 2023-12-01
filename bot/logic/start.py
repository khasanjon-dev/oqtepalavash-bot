from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.data import data
from bot.utils.keyboardbuilder import keyboard_builder
from bot.utils.states import states

router = Router(name='start')


@router.message(CommandStart())
async def language_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(states.language)
    languages = data['languages']
    reply_markup = await keyboard_builder(languages, [1])
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


@router.message(states.language)
async def language_handler(message: types.Message, state: FSMContext) -> None:
    languages = data['languages']
    if message.text in languages:
        await state.set_state(states.city)
    cities = data['cities']
    reply_markup = await keyboard_builder(cities, [2])
    await message.answer('Shaharni tanlang', reply_markup=reply_markup)
