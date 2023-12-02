from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from bot.data import data
from bot.utils.inlinekeyboardbuilder import inline_keyboard_builder
from bot.utils.states import menu_states

menu_router = Router()


async def menu_message(message: types.Message) -> None:
    await message.answer('Buyurtmani birga joylashtiramizmi? 🤗')


@menu_router.message(menu_states.first_menu)
async def first_menu_handler(message: types.Message, state: FSMContext) -> None:
    text = 'Quyidagilardan birini tanlang'
    markup = inline_keyboard_builder(data['menus']['texts'], data['menus']['call_backs'], [1, 2, 1, 2])
    await state.set_state(menu_states.menu)
    await message.answer(text, reply_markup=markup)


@menu_router.message(menu_states.menu)
async def menu_handler(message: types.Message, state: FSMContext) -> None:
    await menu_message(message)
    if message.text == '/start':
        await state.set_state(menu_states.first_menu)
        await first_menu_handler(message, state)
    else:
        text = ("Buyurtma berishni boshlash uchun 🛒\n"
                "Buyurtma qilish tugmasini bosing\n\n"
                "Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin\n\n"
                "<a href='https://telegra.ph/Taomnoma-09-30'>Oqtepa Lavash menu</a>")
        markup = inline_keyboard_builder(data['menus']['texts'], data['menus']['call_backs'], [1, 2, 1, 2])
        await message.answer(text, ParseMode.HTML, reply_markup=markup)
