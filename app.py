from handlers.users import user_router
from loader import bot, dp


if __name__ == '__main__':
    dp.include_router(router=user_router)
    dp.run_polling(bot)
