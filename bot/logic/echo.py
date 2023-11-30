from aiogram import Router, types

echo_router = Router(name='echo')


@echo_router.message()
async def echo_handler(message: types.Message):
    return await message.answer(message.text)
