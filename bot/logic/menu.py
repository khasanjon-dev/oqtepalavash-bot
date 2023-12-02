from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from bot.data import data
from bot.utils.inlinekeyboardbuilder import inline_keyboard_builder
from bot.utils.states import states

menu = Router()


@menu.message(states.menu)
async def menu_handler(message: types.Message, state: FSMContext) -> None:
    text = (f"Buyurtma berishni boshlash uchun 🛒\n"
            f"Buyurtma qilish tugmasini bosing\n\n"
            f"Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin\n\n"
            f"<a href='https://telegra.ph/Taomnoma-09-30'>Oqtepa Lavash menu</a>")
    markup = await inline_keyboard_builder(data['menus'], [1, 2, 1, 2])
    await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=markup)
    await state.clear()

