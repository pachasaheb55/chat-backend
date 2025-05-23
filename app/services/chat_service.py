from app.db.mongo import chats_collection
from app.models.chat import *
from uuid import uuid4
from datetime import datetime

async def create_chat(account_id: str, name: str):
    chat_id = str(uuid4())
    chat = {
        "chat_id": chat_id,
        "account_id": account_id,
        "name": name,
        "created_at": datetime.utcnow(),
        "active": True,
        "branches": [],
        "messages": []
    }
    await chats_collection.insert_one(chat)
    return chat

async def get_chat(chat_id: str):
    return await chats_collection.find_one({"chat_id": chat_id})

async def add_message(data: AddMessageRequest):
    chat = await get_chat(data.chat_id)
    if not chat:
        return None
    qa_pair = {
        "question": data.question,
        "response": data.response,
        "response_id": str(uuid4()),
        "timestamp": datetime.utcnow()
    }
    await chats_collection.update_one(
        {"chat_id": data.chat_id},
        {"$push": {"messages": qa_pair}}
    )
    return qa_pair

async def create_branch(data: CreateBranchRequest, account_id: str):
    parent_chat = await get_chat(data.parent_chat_id)
    if not parent_chat:
        return None

    new_chat_id = str(uuid4())
    new_messages = parent_chat["messages"][:data.message_index + 1]

    new_chat = {
        "chat_id": new_chat_id,
        "account_id": account_id,
        "name": data.name,
        "created_at": datetime.utcnow(),
        "active": True,
        "branches": [],
        "messages": new_messages
    }

    await chats_collection.insert_one(new_chat)

    await chats_collection.update_one(
        {"chat_id": data.parent_chat_id},
        {"$push": {"branches": {"message_index": data.message_index, "branch_chat_id": new_chat_id}}}
    )

    return new_chat

async def get_branches(chat_id: str):
    chat = await get_chat(chat_id)
    return chat.get("branches", []) if chat else None

async def set_active_branch(chat_id: str):
    await chats_collection.update_many({"account_id": (await get_chat(chat_id))["account_id"]}, {"$set": {"active": False}})
    await chats_collection.update_one({"chat_id": chat_id}, {"$set": {"active": True}})
    return await get_chat(chat_id)
