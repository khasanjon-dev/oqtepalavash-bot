from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

product_router = Router()


@product_router.callback_query()
async def product_menu(callback_query: CallbackQuery, state: FSMContext) -> None:
    pass
