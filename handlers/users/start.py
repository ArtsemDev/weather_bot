from aiogram import Router, F
from aiogram.types import Message

from utils.models import User
from keyboards.reply import weather_rkb

start_router = Router()


@start_router.message(F.text == '/start')
async def start_command(message: Message):
    await message.delete()
    user = await User.get(message.from_user.id)
    if user:
        await message.answer(
            text=f'Hello {message.from_user.username}!',
            reply_markup=weather_rkb
        )
    else:
        user = User(id=message.from_user.id)
        await user.save()
        await message.answer(
            text=f'Hello {message.from_user.username}! Nice to meet you!',
            reply_markup=weather_rkb
        )
