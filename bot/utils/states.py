from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    language = State()
    city = State()
    phone = State()


states = States()
