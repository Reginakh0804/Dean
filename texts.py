MESSAGES = {
    "ru": {
        "language": ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("Ru Русский"),
            KeyboardButton("us English"),
            KeyboardButton("uz O‘zbekcha")
        ),
        "get_phone": "📲 Пожалуйста, отправьте свой номер телефона.",
        "phone": ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("📞 Отправить номер телефона", request_contact=True)
        ),
        "ask_name": "👤 Пожалуйста, введите ваше полное имя.",
        "ask_group": "🏷️ Пожалуйста, укажите номер вашей учебной группы.",
        "ask_message": "📝 Напишите своё обращение.",
        "done": "✅ Спасибо! Ваше обращение зарегистрировано."
    },

    "uz": {
        "language": ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("Ru Ruscha"),
            KeyboardButton("us Inglizcha"),
            KeyboardButton("uz O‘zbekcha")
        ),
        "get_phone": "📲 Iltimos, telefon raqamingizni yuboring.",
        "phone": ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("📞 Telefon raqamni yuborish", request_contact=True)
        ),
        "ask_name": "👤 Iltimos, to‘liq ismingizni kiriting.",
        "ask_group": "🏷️ Guruh raqamingizni kiriting.",
        "ask_message": "📝 Murojaatingizni yozing.",
        "done": "✅ Rahmat! Murojaatingiz qabul qilindi."
    },

    "en": {
        "language": ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("Ru Russian"),
            KeyboardButton("us English"),
            KeyboardButton("uz Uzbek")
        ),
        "get_phone": "📲 Please send your phone number.",
        "phone": ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("📞 Share phone number", request_contact=True)
        ),
        "ask_name": "👤 Enter your full name.",
        "ask_group": "🏷️ Enter your group number.",
        "ask_message": "📝 Write your message.",
        "done": "✅ Thank you! Your request has been registered."
    }
}
