from fastapi import APIRouter, Depends, HTTPException
from app.models.chat import *
from app.services import chat_service
from app.auth.auth import get_current_user
from fastapi import Depends

router = APIRouter(prefix="/api/v1")

from bson import ObjectId

def convert_object_id(document):
    if "_id" in document:
        document["_id"] = str(document["_id"])
    return document


@router.post("/chats/create-chat")
async def create_chat(data: ChatCreate, user=Depends(get_current_user)):
    # import pdb; pdb.set_trace()
    # print("Authenticated user:", user["username"])
    result = await chat_service.create_chat(user["account_id"], data.name)
    return convert_object_id(result)


@router.get("/chats/get-chat")
async def get_chat(chat_id: str, user=Depends(get_current_user)):
    chat = await chat_service.get_chat(chat_id)
    if not chat: raise HTTPException(404, "Chat not found")
    return convert_object_id(chat)

@router.post("/messages/add-message")
async def add_message(data: AddMessageRequest, user=Depends(get_current_user)):
    result = await chat_service.add_message(data)
    if not result: raise HTTPException(404, "Chat not found")
    return convert_object_id(result)

@router.post("/branches/create-branch")
async def create_branch(data: CreateBranchRequest, user=Depends(get_current_user)):
    # new_branch = await chat_collection.find_one({"_id": new_branch_id})
    # new_branch["_id"] = str(new_branch["_id"])  # <== add this line
    # return new_branch
    result = await chat_service.create_branch(data, user["account_id"])
    return convert_object_id(result)

@router.get("/branches/get-branches")
async def get_branches(chat_id: str, user=Depends(get_current_user)):
    result = await chat_service.get_branches(chat_id)
    return convert_object_id(result)

@router.put("/branches/set-active-branch")
async def set_active_branch(chat_id: str, user=Depends(get_current_user)):
    result = await chat_service.set_active_branch(chat_id)
    return convert_object_id(result)