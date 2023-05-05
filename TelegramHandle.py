import GPT
import time
from telegram import Bot
from telegram.constants import ParseMode
from telegram import InputMediaPhoto
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
bot = Bot(token='5944099789:AAGuMRTclKHmkxxziNXudd9H3bElOJSwOSA')
mes = """Idea: A virtual interior design platform that utilizes virtual and augmented reality to create personalized and immersive experiences for clients. 

Problem: Traditional interior design processes can be time-consuming, expensive and require in-person meetings, limiting options for remote clients. 

Target Audience: Homeowners, renters, and businesses looking to redesign their space using technology to improve the process. 

Revenue Model: Subscription-based service with varying levels of personalized design options. Additional revenue potential through partnerships with home decor companies for commerce integration and opportunities for virtual product placement. """
async def send_telegram_message():
    await bot.send_photo(chat_id='@testAutoTelegram',  caption=mes, photo="https://i.stack.imgur.com/taBnv.png")
asyncio.run(send_telegram_message())

