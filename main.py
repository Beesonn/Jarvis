import subprocess
import time
import threading
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from vars import TOKEN, WEBHOOK, URL
from bot import *
import aiohttp
import asyncio


async def alive_task():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(URL, timeout=5) as response:
                    pass
            except Exception as e:
                print(f"Error in alive_task: {e}")
            await asyncio.sleep(10)
            

def main():
    if WEBHOOK:
        subprocess.Popen(["gunicorn", "app:app"])    
    if URL:
        loop = asyncio.get_event_loop()
        loop.create_task(alive_task())
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("newchat", newchat))
    application.add_handler(MessageHandler(filters.TEXT | filters.PHOTO & ~filters.COMMAND, chat, block=False))
    application.run_polling()
  
main()
