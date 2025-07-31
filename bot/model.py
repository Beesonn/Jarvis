from mango import Mango
from database import *

def ai_response(model: str = "gpt-4o", messages: list = []):
    client = Mango(api_key="")
  
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return response

def ai_chat(m):
    client = Mango(api_key="")
    messages = get_conv(m.from_user.id)
    messages.append({"role": "user", "content": m.text})
    response = ai_response(
        model=model,
        messages=messages
    )
    messages.append({"role": "assistant", "content":, response.choices[0].message.content})
    set_conv(messages)
    return response
