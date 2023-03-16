from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


weather_rkb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    keyboard=[
        [
            KeyboardButton(text='ПО ЛОКАЦИИ', request_location=True),
        ]
    ]
)
