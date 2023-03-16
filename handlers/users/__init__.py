from aiogram import Router

from .start import start_router
from .weather import weather_router


user_router = Router()
user_router.include_router(router=start_router)
user_router.include_router(router=weather_router)
