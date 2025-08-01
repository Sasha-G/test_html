import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('8123870873:AAEZBPLR3KCu6pi_cJ6sDS4rCcfrJLNduf8')
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text='Открыть веб сайт',web_app=WebAppInfo(url='https://www.youtube.com/watch?v=y65BZbNB0YA&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=9'))],],resize_keyboard=True)
    await message.answer('Привет! Откройте веб-сайт:', reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())