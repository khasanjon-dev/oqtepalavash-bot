from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.data import data
from bot.requests.user import get_or_create_user
from bot.utils.keyboardbuilder import keyboard_builder
from bot.utils.states import states

router = Router(name='start')


@router.message(states.phone)
async def phone_handler(message: types.Message, state: FSMContext) -> None:
    if message.content_type == types.ContentType.CONTACT:
        pass
    elif message.text.startswith('+998') and len(message.text) == 13:
        pass


@router.message(states.city)
async def city_handler(message: types.Message, state: FSMContext) -> None:
    if message.text in data['cities']:
        # await state.set_state(states.phone)
        await state.clear()
        text = ("Ro'yxatga olish uchun telefon raqamingizni kiriting!\n"
                "Masalan +998xx xxx xx xx")
        button = KeyboardButton(text="📞Mening telefon raqamim", request_contact=True)
        markup = ReplyKeyboardBuilder().add(button).as_markup(resize_keyboard=True)
        await message.answer(text, reply_markup=markup)
    else:
        await state.set_state(states.city)


@router.message(states.language)
async def language_handler(message: types.Message, state: FSMContext) -> None:
    if message.text in data['languages']:
        context = {
            'telegram_id': message.from_user.id,
            'language': message.text
        }
        await get_or_create_user(context)
        await state.set_state(states.city)
        reply_markup = await keyboard_builder(data['cities'], [2])
        await message.answer('Shaharni tanlang', reply_markup=reply_markup)
    else:
        await state.set_state(states.start)
        await start_handler(message, state)


@router.message(states.start)
async def start_handler(message: types.Message, state: FSMContext) -> None:
    if message.text in data['languages']:
        await state.set_state(states.language)
        await language_handler(message, state)
    else:
        await state.set_state(states.start)
        reply_markup = await keyboard_builder(data['languages'], [1])
        text = (
            "Muloqot tilini tanlang\n"
            "Выберите язык\n"
            "Select Language"
        )
        await message.answer(text, reply_markup=reply_markup)


@router.message(CommandStart())
async def first_start_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(states.start)
    context = {
        'telegram_id': message.from_user.id
    }
    await get_or_create_user(context)
    user = message.from_user
    text = (f"Assalomu alaykum {user.first_name}. Men Oqtepa Lavash yetkazib berish xizmati botiman!\n"
            f"Привет {user.first_name}! Я бот службы доставки Oqtepa Lavash!\n"
            f"Hi {user.first_name}! I am Oqtepa Lavash delivery service bot!")
    await message.answer(text)
    await start_handler(message, state)
