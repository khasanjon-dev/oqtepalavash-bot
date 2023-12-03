from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.data import data
from bot.utils.inlinekeyboardbuilder import MenuCallBack
from bot.utils.keyboardbuilder import keyboard_builder
from bot.utils.states import order_states

callback_router = Router(name='callback_data')
order_router = Router(name='order_router')


@order_router.message(order_states.location)
async def order_get_location(message: types.Message, state: FSMContext) -> None:
    if message.content_type == types.ContentType.LOCATION:
        context = {
            'longitude': message.location.longitude,
            'latitude': message.location.latitude
        }
        data = await state.get_data()
        await message.answer(f'Joylashuv qabul qilindi!\n{data}')

    else:
        text = f"{state.get_data()} uchun geo-joylashuvni jo'nating yoki manzilni tanlang"
        builder = ReplyKeyboardBuilder()
        markup = builder.add(KeyboardButton(text='📍 Geo-joylashuvni yuborish', request_location=True))
        await message.answer(text, reply_markup=markup.as_markup(resize_keyboard=True))


@order_router.message(order_states.menu)
async def order_menu_handler(message: types.Message, state: FSMContext) -> None:
    if message.text in data['delivery_menu']:
        await state.set_state(order_states.location)
        await state.update_data(reception_type=data['delivery_menu'].get(message.text, None))
        await order_get_location(message, state)
    else:
        markup = keyboard_builder(data['delivery_menu'].keys(), [2])
        await message.answer('Buyurtma turini tanlang', reply_markup=markup)


@callback_router.callback_query(MenuCallBack.filter(F.choice == 'order'))
async def order_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(order_states.menu)
    await state.update_data(order_menu=callback_query.data.split(':')[-1])
    await order_menu_handler(callback_query.message, state)
