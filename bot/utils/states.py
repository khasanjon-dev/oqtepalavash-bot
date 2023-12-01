from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    start = State()
    language = State()
    city = State()
    phone = State()


states = States()
