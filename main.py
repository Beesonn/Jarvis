import subprocess
import time
import threading
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from vars import TOKEN, WEBHOOK, URL
from bot import *


def alive_task():
    while True:
        try:
            requests.get(URL, timeout=5)
        except:
            pass
        time.sleep(10)
        

def main():
    if WEBHOOK:
        subprocess.Popen(["gunicorn", "app:app"])    
    if URL:
        threading.Thread(target=alive_task, daemon=True).start()
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("newchat", newchat))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat, block=False))
    application.run_polling()
  
main()
