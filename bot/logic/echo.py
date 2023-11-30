from random import randint

from aiogram import F
from aiogram import Router, types
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

echo_router = Router(name='echo')


@echo_router.message(F.text == 'hi')
async def echo_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    for i in range(1, 17):
        builder.add(InlineKeyboardButton(text=str(i), callback_data=str(i)))
    builder.adjust(6, 4, 3)
    await message.answer(message.text, reply_markup=builder.as_markup(resize_keyboard=True))


@echo_router.callback_query(F.data == '10')
async def send_random_link(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer(text=f'Thanks {callback.from_user.first_name, callback.from_user.username}', show_alert=True)
