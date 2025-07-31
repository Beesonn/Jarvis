from database import *
from telegram.ext import ContextTypes
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    text = (
        f"Hello <a href='tg://user?id={update.message.from_user.id}'>{update.message.from_user.first_name}</a>! 👋\n\n"
        "I'm <b>Jarvis</b>, your intelligent assistant here to help you anytime. 😊\n\n"
        "Just send a message to begin chatting!"
    )
    
    keyboard = [
        [InlineKeyboardButton("Join Support Group", url="https://t.me/XBOTSUPPORTS")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text, parse_mode="HTML", reply_markup=reply_markup)
  
