from typing import Any

from aiogram import Router, types, html
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.data import data
from bot.utils.keyboardbuilder import keyboard_builder
from bot.utils.states import states

router = Router(name='start')


@router.message(Command(commands=['start']))
async def start_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(states.language)
    user =
    # TODO  request to api
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
        await state.update_data(language=message.text)
        await state.set_state(states.city)
    cities = data['cities']
    reply_markup = await keyboard_builder(cities, [2])
    await message.answer('Shaharni tanlang', reply_markup=reply_markup)


@router.message(states.city)
async def city_handler(message: types.Message, state: FSMContext) -> None:
    if message.text in data['cities']:
        await state.update_data(city=message.text)
        await state.set_state(states.phone)
    text = ("Ro'yxatga olish uchun telefon raqamingizni kiriting!\n"
            "Masalan +998xx xxx xx xx")
    date = await state.get_data()
    await state.clear()
    button = KeyboardButton(text="📞Mening telefon raqamim", request_contact=True)
    markup = ReplyKeyboardBuilder().add(button).as_markup(resize_keyboard=True)
    await message.answer(text, data=date, reply_markup=markup)

