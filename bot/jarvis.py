from mango import AsyncMango
from vars import API_KEY

client = AsyncMango(api_key=API_KEY)  

    
async def get_response(messages: list, model: str):            
    response = await client.chat.completions.create(
        model=model,
        messages=messages
    )    
    return response.choices[0].message.content
    
