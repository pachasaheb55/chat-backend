from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class QAPair(BaseModel):
    question: str
    response: str
    response_id: str
    timestamp: datetime

class Branch(BaseModel):
    message_index: int
    branch_chat_id: str

class ChatCreate(BaseModel):
    # account_id: str
    name: str

class Chat(BaseModel):
    chat_id: str
    account_id: str
    name: str
    created_at: datetime
    active: bool
    branches: List[Branch]
    messages: List[QAPair]

class AddMessageRequest(BaseModel):
    chat_id: str
    question: str
    response: str

class CreateBranchRequest(BaseModel):
    parent_chat_id: str
    message_index: int
    name: str
