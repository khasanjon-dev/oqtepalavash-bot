from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.data import data
from bot.requests.user import update_or_create_user
from bot.utils.keyboardbuilder import keyboard_builder
from bot.utils.states import states

router = Router(name='start')


# TODO solve the recoursion action
@router.message(states.phone)
async def phone_handler(message: types.Message, state: FSMContext) -> None:
    if message.content_type == types.ContentType.CONTACT:
        context = {
            'telegram_id': message.from_user.id,
            'phone': message.contact.phone_number
        }
        await update_or_create_user(context)
        await state.clear()
        await message.answer('Welcome dear!')
    else:
        text = "Ro'yxatga olish uchun telefon raqamingizni yuboring!"
        button = KeyboardButton(text="📞Mening telefon raqamim", request_contact=True)
        markup = ReplyKeyboardBuilder().add(button).as_markup(resize_keyboard=True)
        await message.answer(text, reply_markup=markup)


@router.message(states.city)
async def city_handler(message: types.Message, state: FSMContext) -> None:
    if message.text in data['cities']:
        context = {
            'telegram_id': message.from_user.id,
            'city': message.text
        }
        await update_or_create_user(context)
        await state.set_state(states.phone)
        await phone_handler(message, state)
    else:
        reply_markup = await keyboard_builder(data['cities'], [2])
        await message.answer('Shaharni tanlang', reply_markup=reply_markup)


@router.message(states.language)
async def language_handler(message: types.Message, state: FSMContext) -> None:
    if message.text in data['languages']:
        context = {
            'telegram_id': message.from_user.id,
            'language': message.text
        }
        await update_or_create_user(context)
        await state.set_state(states.city)
        await city_handler(message, state)
    else:
        reply_markup = await keyboard_builder(data['languages'], [1])
        text = (
            "Muloqot tilini tanlang\n"
            "Выберите язык\n"
            "Select Language"
        )
        await message.answer(text, reply_markup=reply_markup)


#

@router.message(CommandStart())
async def first_start_handler(message: types.Message, state: FSMContext) -> None:
    context = {
        'telegram_id': message.from_user.id
    }
    await update_or_create_user(context)
    user = message.from_user
    text = (f"Assalomu alaykum {user.first_name}. Men Oqtepa Lavash yetkazib berish xizmati botiman!\n"
            f"Привет {user.first_name}! Я бот службы доставки Oqtepa Lavash!\n"
            f"Hi {user.first_name}! I am Oqtepa Lavash delivery service bot!")
    await message.answer(text)
    await state.set_state(states.language)
    await language_handler(message, state)
