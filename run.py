import asyncio

from config import TOKEN

from aiogram import Bot, Dispatcher


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    await dp.start_polling(bot)






if __name__ == '__main__':
    asyncio.run(main())









