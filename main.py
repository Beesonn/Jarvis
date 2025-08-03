from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from vars import TOKEN, WEBHOOK, URL
from bot import *
import subprocess


def main():
    if WEBHOOK:
        subprocess.Popen(["gunicorn", "app:app"])    
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("newchat", newchat))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat, block=False))
    application.run_polling()
  
main()
