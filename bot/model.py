from mango import Mango

def ai_response(model: str = "gpt-4o", messages: list = []):
    client = Mango(api_key="")
  
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return response
