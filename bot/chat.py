from jarvis import get_response
from telegram import Update
from telegram.ext import ContextTypes

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m = update.message
    response = get_response(m)        
    if m.reply_to_message and m.reply_to_message.from_user.id == context.bot.id or context.bot.username.lower() in m.text.lower() or m.chat.type != "private":
        await m.reply_text(response.replace("**", "*"), parse_mode="markdown")                
