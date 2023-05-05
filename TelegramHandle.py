import GPT
from telegram import Bot
from telegram.constants import ParseMode
from telegram import InputMediaPhoto
import asyncio
bot = Bot(token='5944099789:AAGuMRTclKHmkxxziNXudd9H3bElOJSwOSA')
status = bot.send_message(chat_id='@testAutoTelegram', text=GPT.get_idea(), parse_mode=ParseMode.HTML)
asyncio.run(status)