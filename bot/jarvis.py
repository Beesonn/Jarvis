from mango import Mango
import datetime
from vars import API_KEY

client = Mango(api_key=API_KEY)  

    
def get_response(messages: list, model: str):            
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )    
    return response.choices[0].message.content
    
