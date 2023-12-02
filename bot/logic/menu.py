from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from bot.utils.states import states

menu = Router()


@menu.message(states.menu)
async def menu_handler(message: types.Message, state: FSMContext) -> None:
    text = (f"Buyurtma berishni boshlash uchun 🛒\n"
            f"Buyurtma qilish tugmasini bosing\n\n"
            f"Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin\n\n"
            f"<a href='https://telegra.ph/Taomnoma-09-30'>Oqtepa Lavash menu</a>")
    await message.answer(text, parse_mode=ParseMode.HTML)
    await state.clear()
