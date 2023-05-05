import GPT
import ImageSearch
import time
from telegram import Bot
from telegram.constants import ParseMode
from telegram import InputMediaPhoto
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
bot = Bot(token='5944099789:AAGuMRTclKHmkxxziNXudd9H3bElOJSwOSA')
async def send_telegram_message():
    response, prompt = GPT.get_idea()
    n = 0
    try:
        await bot.send_photo(chat_id='@testAutoTelegram',  caption=response, photo=ImageSearch.get_image(prompt,n))
    except:
        n+=1
        await bot.send_photo(chat_id='@testAutoTelegram', caption=response, photo=ImageSearch.get_image(prompt,n))
asyncio.run(send_telegram_message())

