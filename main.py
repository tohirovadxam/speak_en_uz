import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from googletrans import Translator
from get_info import give_all_info

BOT_TOKEN =  os.getenv('TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("Welcome to my Speak English bot. Enter any word ('en' or 'uz'): ")

@dp.message(Command('help'))
async def help_(message: Message):
    await message.answer("If you need any help, just ask from user @adxam04!!!")

@dp.message()
async def give_the_result(message: Message):
    async with Translator() as tr:
        if message.text:
            lang = await tr.detect(message.text)
            if lang.confidence < 0.3:
                await message.reply("WORD NOT FOUND!!!")
                return
            if lang.lang == 'uz':
                translated = await tr.translate(message.text, dest='en', src='uz')
                await message.reply(translated.text)

            elif lang.lang == 'en':
                if len(message.text.split()) > 1:
                    translated = await tr.translate(message.text, dest='uz', src='en')
                    await message.reply(translated.text)
                else:
                    all_info = give_all_info(message.text)
                    await message.reply(all_info['definitions'])
                    if all_info.get('audio'):
                        await message.reply_audio(all_info['audio'])

        else:
            await message.reply("This one is empty. Please enter any word : ")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
