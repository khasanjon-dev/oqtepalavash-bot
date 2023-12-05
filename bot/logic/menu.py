from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from bot.data import data, menu_data
from bot.utils.callback_class import MenuCallBack, MainMenuCallBack
from bot.utils.inlinekeyboardbuilder import inline_keyboard_builder
from bot.utils.states import menu_states

menu_router = Router()


async def menu_message(message: types.Message) -> None:
    await message.answer('Buyurtmani birga joylashtiramizmi? 🤗', reply_markup=ReplyKeyboardRemove())


@menu_router.message(menu_states.first_menu)
async def first_menu_handler(message: types.Message, state: FSMContext) -> None:
    text = 'Quyidagilardan birini tanlang 👇'
    markup = inline_keyboard_builder(MenuCallBack, data['menu'].keys(), data['menu'].values(), [1, 2, 1, 2])
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
        markup = inline_keyboard_builder(MenuCallBack, data['menu'].keys(), data['menu'].values(), [1, 2, 1, 2])
        await message.answer(text, ParseMode.HTML, reply_markup=markup)


@menu_router.message(menu_states.main_menu)
async def main_menu_handler(msg: types.Message, state: FSMContext):
    if msg.text == '/start':
        await state.set_state(menu_states.menu)
        await menu_handler(msg, state)
    else:
        await menu_message(msg)
        text = ("Buyurtma qaytadan boshlash uchun 🆕 Yangi buyurtma yaratish tugmasini bosing\n\n"
                "Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin\n\n"
                "<a href='https://telegra.ph/Taomnoma-09-30'>Oqtepa Lavash menu</a>")
        markup = inline_keyboard_builder(
            MainMenuCallBack,
            menu_data['main_menu'].keys(),
            menu_data['main_menu'].values(),
            [1, 2, 1, 2, 1]
        )
        await msg.answer(text, ParseMode.HTML, reply_markup=markup)
