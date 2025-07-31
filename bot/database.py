from pymongo import MongoClient
from vars import DB_URL

client = MongoClient(DB_URL)
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

def get_user(id: int):
    us = user.find_one({"id": id})
    return us.get("messages", [])

def add_user(id: int):
    if not user.find_one({"id": id}):    
        user.insert_one({"id": id, "messages": []})

def add_chat(id: int):
    if not chats.find_one({"id": id}):    
        chats.insert_one({"id": id})
