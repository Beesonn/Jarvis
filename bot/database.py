from pymongo import MongoClient

client = MongoClient("")
db = client["jarvis"]

chats = db["chats"]
user = db["users"]

def set_conv(id: int, messages: dict):
    user.update_one(
        {"id": id},
        {"$push": {"messages": messages}},  
        upsert=True
    )

def delete_conv(id: int):
    if user.find_one({"id": id}):
        user.update_one(
            {"id": id},
            {"$set": {"messages": []}}  
        )
        return True
    return False

def set_model(model: str):
    user.update_one(
        {"id": id},
        {"$set": {"model": model}},  
        upsert=True
    )

def add_user(id: int):
    if not user.find_one({"id": id}):    
        user.insert_one({"id": id, "messages": [], "model": "gpt-4o"})

def add_chat(id: int):
    if not chats.find_one({"id": id}):    
        chats.insert_one({"id": id})
