from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    language = State()
    city = State()
    phone = State()
    confirm_code = State()


states = States()
