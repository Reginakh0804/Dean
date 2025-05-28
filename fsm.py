from aiogram.dispatcher.filters.state import State, StatesGroup

class Register(StatesGroup):
    Language = State()
    Phone = State()
    Name = State()
    Group = State()
    Message = State()
