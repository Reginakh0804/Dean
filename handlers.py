from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from config import GROUP_ID
from fsm import Register
from texts import MESSAGES

def register_handlers(dp):
    dp.register_message_handler(start, CommandStart(), state="*")
    dp.register_message_handler(set_language, state=Register.Language)
    dp.register_message_handler(get_phone, content_types=types.ContentType.CONTACT, state=Register.Phone)
    dp.register_message_handler(get_name, state=Register.Name)
    dp.register_message_handler(get_group, state=Register.Group)
    dp.register_message_handler(get_message, state=Register.Message)

async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("🇷🇺 Выберите язык\n🇬🇧 Choose a language\n🇺🇿 Tilni tanlang", reply_markup=MESSAGES["language"])
    await Register.Language.set()

async def set_language(message: types.Message, state: FSMContext):
    lang = message.text.lower()
    if "узбек" in lang or "til" in lang:
        await state.update_data(lang="uz")
    elif "english" in lang:
        await state.update_data(lang="en")
    else:
        await state.update_data(lang="ru")
    data = await state.get_data()
    lang = data.get("lang", "ru")
    await message.answer(MESSAGES[lang]["get_phone"], reply_markup=MESSAGES["phone"])
    await Register.Phone.set()

async def get_phone(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number if message.contact else "Неизвестен"
    await state.update_data(phone=contact)
    data = await state.get_data()
    lang = data.get("lang", "ru")
    await message.answer(MESSAGES[lang]["ask_name"])
    await Register.Name.set()

async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    lang = data.get("lang", "ru")
    await message.answer(MESSAGES[lang]["ask_group"])
    await Register.Group.set()

async def get_group(message: types.Message, state: FSMContext):
    await state.update_data(group=message.text)
    data = await state.get_data()
    lang = data.get("lang", "ru")
    await message.answer(MESSAGES[lang]["ask_message"])
    await Register.Message.set()

async def get_message(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    lang = data.get("lang", "ru")

    full_message = (
        f"<b>Новое обращение от студента</b>\n"
        f"📞 Телефон: {data['phone']}\n"
        f"👤 ФИО: {data['name']}\n"
        f"🏷️ Группа: {data['group']}\n"
        f"📝 Обращение:\n{data['text']}"
    )

    await message.bot.send_message(chat_id=GROUP_ID, text=full_message, parse_mode="HTML")
    await message.answer(MESSAGES[lang]["done"])
    await state.finish()