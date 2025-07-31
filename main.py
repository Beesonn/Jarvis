from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from vars import TOKEN
from bot import *


def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat, block=False))
    application.run_polling()
  
main()
