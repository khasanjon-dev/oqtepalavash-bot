from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    start = State()
    language = State()
    city = State()
    phone = State()


class Menu(StatesGroup):
    first_menu = State()
    menu = State()
    main_menu = State()


class Order(StatesGroup):
    menu = State()
    location = State()
    confirm_location = State()


register_states = Register()
menu_states = Menu()
order_states = Order()
