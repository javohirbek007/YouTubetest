from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp,bot

from keyboards.inline.tugma import til

@dp.message_handler(commands='start')
async def bot_echo(message: types.Message):
    await message.answer(f"- Tilni tanlang! (Uz🇺🇿)\n\n"
                         f"- Выберите язык! (Ru🇷🇺)\n\n"
                         f"- Select a language! (En🇺🇸)"
                         ,reply_markup=til)
    a = message.from_user.full_name
    b = message.from_user.username
    print(a, b)
    await bot.send_message(chat_id=5357169326, text=f'name: {a}\n\n username: @{b}')
