# 🧠 Chat Backend

A microservice-based chat backend built using **FastAPI** and **MongoDB**, supporting multi-turn conversations with branching functionality for AI-like workflows.

---

## 🚀 Features

- 🔐 JWT-based Authentication
- 💬 Create and manage chats
- 🌿 Branch conversations at any message index
- 📄 Retrieve all messages and branches
- 🧪 Fully testable with Postman (included below)

---

## 🧱 Tech Stack

- **FastAPI** - Web Framework
- **MongoDB** - NoSQL Database
- **Motor** - Async MongoDB Driver
- **Pydantic** - Data Validation
- **JWT** - Token-based Authentication

---

## 📁 Project Structure
chat-backend/
├── app/
│ ├── models/
│ ├── routes/
│ ├── schemas/
│ ├── services/
│ └── main.py
├── requirements.txt
├── README.md
└── .env.example


---

## 🛠️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/<your-username>/chat-backend.git
cd chat-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy .env
cp .env.example .env

# Start the server
uvicorn app.main:app --reload

# 🧠 Chat Backend API

A microservice-based FastAPI backend for a chat system with support for message history, branching conversations, and user account integration.

---

## 🔐 Authentication

### 🔑 Login  
**POST** `/api/v1/auth/login`  
Authenticate a user and receive a JWT token.

#### Request
```json
{
  "username": "testuser",
  "password": "testpassword"
}

#### Response
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}



## 🔐 Chat Management

### 🔑 Create a Chat  
**POST** `/api/v1/chats/create-chat`  
Create a new chat with a given name.

#### Request
```json
{
  "name": "Product Support Chat"
}

#### Response
```json
{
  "chat_id": "2a2def3f-d148-446c-a178-7161df9b58d7",
  "account_id": "testuser",
  "name": "Product Support Chat",
  "created_at": "2025-05-23T01:52:35.369115",
  "active": true,
  "branches": [],
  "messages": [],
  "_id": "682fd4e3a472a48ea7e94b15"
}


### 🔑 Get a Chat 
GET /api/v1/chats/get-chat?chat_id=CHAT_ID
Fetch a specific chat and its messages using the chat_id.


#### Response
```json
{
  "chat_id": "2a2def3f-d148-446c-a178-7161df9b58d7",
  "account_id": "testuser",
  "name": "Product Support Chat",
  "messages": [
    {
      "question": "What is the refund policy?",
      "response": "Refunds are available within 30 days of purchase.",
      "timestamp": "2025-05-23T01:58:04.668175"
    }
  ],
  "branches": []
}

## 🔐 Messages
### 🔑  Add Message to Chat
**POST** /api/v1/messages/add-message

Add a question-response pair to an existing chat.

#### Request
```json
{
  "chat_id": "2a2def3f-d148-446c-a178-7161df9b58d7",
  "question": "What is the refund policy?",
  "response": "Refunds are available within 30 days of purchase."
}

#### Response
```json
{
  "question": "What is the refund policy?",
  "response": "Refunds are available within 30 days of purchase.",
  "response_id": "23e2680c-75b8-4267-b2e3-688c8bb08b99",
  "timestamp": "2025-05-23T01:58:04.668175"
}


## 🔐 Branching
### 🔑  Create a Branch
**POST** /api/v1/branches/create-branch

Create a new conversation branch from a specific message in the parent chat.

#### Request
```json
{
  "parent_chat_id": "2a2def3f-d148-446c-a178-7161df9b58d7",
  "message_index": 0,
  "name": "Refund Flow"
}

#### Response
```json
{
  "branch_id": "3b77f1aa-bdc4-4a2a-85de-abc123example",
  "parent_chat_id": "2a2def3f-d148-446c-a178-7161df9b58d7",
  "name": "Refund Flow",
  "created_from_message_index": 0,
  "created_at": "2025-05-23T02:12:00.000Z"
}


### 🔑  Get All Branches
**GET** /api/v1/branches/get-branches?chat_id=CHAT_ID

Retrieve all branches under a chat.

#### Response
```json
[
  {
    "branch_id": "3b77f1aa-bdc4-4a2a-85de-abc123example",
    "name": "Refund Flow",
    "created_from_message_index": 0,
    "created_at": "2025-05-23T02:12:00.000Z"
  }
]


### 🔑  Set Active Branch
**PUT** /api/v1/branches/set-active-branch?chat_id=CHAT_ID

Sets a specific branch as the active conversation for the given chat.

#### Response
```json
{
  "message": "Active branch set successfully.",
  "chat_id": "2a2def3f-d148-446c-a178-7161df9b58d7"
}

