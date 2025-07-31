from pymongo import MongoClient

client = MongoClient("")  
db = client["jarvis"]  

chats = db["chats"]
user = db["users"]      
conv = db["conv"]

def set_conv(id: int, messages: dict):
    conv.update_one(
        {"id": id},
        {"$push": {"messages": messages}},  
        upsert=True
    )
    
def delete_conv(id: int):
    if conv.find_one({"id": id}):
        conv.delete_one({"id": id})
        return True
    return False

def add_user(id: int):
    if not user.find_one({"id": id}):    
        user.insert_one({"id": id})

def add_chat(id: int):
    if not chats.find_one({"id": id}):    
        chats.insert_one({"id": id})
