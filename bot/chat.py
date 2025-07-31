from jarvis import get_response

async def chat(update, context):
    m = update.message
    response = get_response(m)        
    if context.bot.username in m.text.lower():
        await m.reply_text(response.replace("**", "*"), parse_mode="markdown")    
    if m.chat.type != "private"         
        await m.reply_text(response.replace("**", "*"), parse_mode="markdown")    
    
