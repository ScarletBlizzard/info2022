from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import aiohttp
from bs4 import BeautifulSoup as Soup


URL = 'https://images.search.yahoo.com/search/images;_ylt=AwrJ.QpoJWljCPIyZvdXNyoA;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZANMT0NVSTA1M0NfMQRzZWMDcGl2cw--?p=%s&fr2=piv-web&fr=yfp-t'
SECRET_TOKEN = '5463869674:AAGESLmAu_zXrdXxpxpSQeWDF3uiBC9HBKo'
bot = Bot(token=SECRET_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Image Bot!")

@dp.message_handler()
async def send_image(message: types.Message):
    req = message.text
    async with aiohttp.ClientSession() as session:
        async with session.get(URL % req) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = Soup(html, 'lxml')
                images = soup.select('img[src]')
                try:
                    img_url = images[0]['src']
                    await bot.send_photo(message.chat.id, photo=img_url)
                except IndexError:
                    await message.reply('Нет картинок по этому запросу.')
                        

if __name__ == '__main__':
    executor.start_polling(dp)
