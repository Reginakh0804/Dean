
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

MESSAGES = {
    "language": ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("🇷🇺 Русский"),
        KeyboardButton("🇺🇸 English"),
        KeyboardButton("🇺🇿 O'zbekcha")
    ),
    "get_phone": "📱 Пожалуйста, отправьте свой номер телефона.",
    "phone": ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("📞 Отправить номер телефона", request_contact=True)
    ),
    "ask_name": "👤 Пожалуйста, введите ваше полное имя.",
    "ask_group": "🏷️ Пожалуйста, укажите номер вашей учебной группы.",
    "ask_message": "📝 Напишите своё обращение.",
    "done": "✅ Спасибо! Ваше обращение зарегистрировано."
}
