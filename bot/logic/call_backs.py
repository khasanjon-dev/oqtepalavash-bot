from aiogram import Router, F, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.data import data, orders_data
from bot.logic.menu import main_menu_handler
from bot.utils.callback_class import MenuCallBack
from bot.utils.keyboardbuilder import keyboard_builder
from bot.utils.locations import get_address
from bot.utils.states import order_states, menu_states
from root import bot

callback_router = Router(name='callback_data')
order_router = Router(name='order_router')


@order_router.message(order_states.confirm_location)
async def confirm_location_handler(message: types.Message, state: FSMContext) -> None:
    if message.text in orders_data['confirm_menu']:
        await state.set_state(menu_states.main_menu)
        await main_menu_handler(message, state)
    else:
        markup = keyboard_builder(orders_data['confirm_menu'], [2])
        address = get_address(message.location.latitude, message.location.longitude)
        text = f'Joylashuv qabul qilindi!\n<b>{address}</b>\nUshbu manzilni tasdiqlaysizmi?'
        await message.answer(text, ParseMode.HTML, reply_markup=markup)


@order_router.message(order_states.location)
async def order_get_location_handler(message: types.Message, state: FSMContext) -> None:
    if message.content_type == types.ContentType.LOCATION:
        await state.set_state(order_states.confirm_location)
        await confirm_location_handler(message, state)
    else:
        data = await state.get_data()
        text = f"{data['reception_type'][-1]} uchun geo-joylashuvni jo'nating yoki manzilni tanlang"
        builder = ReplyKeyboardBuilder()
        markup = builder.add(KeyboardButton(text='📍 Geo-joylashuvni yuborish', request_location=True))
        await message.answer(text, reply_markup=markup.as_markup(resize_keyboard=True))


@order_router.message(order_states.menu)
async def order_menu_handler(message: types.Message, state: FSMContext) -> None:
    if message.text in data['delivery_menu']:
        await state.set_state(order_states.location)
        await state.update_data(reception_type=[data['delivery_menu'].get(message.text, None), message.text])
        await order_get_location_handler(message, state)
    else:
        markup = keyboard_builder(data['delivery_menu'].keys(), [2])
        await message.answer('Buyurtma turini tanlang', reply_markup=markup)


@callback_router.callback_query(MenuCallBack.filter(F.choice == 'order'))
async def order_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(order_states.menu)
    await bot.edit_message_text('Buyurtmani birga joylashtiramizmi? 🤗', callback_query.message.chat.id,
                                callback_query.message.message_id)
    await state.update_data(order_menu=callback_query.data.split(':')[-1])
    await order_menu_handler(callback_query.message, state)
