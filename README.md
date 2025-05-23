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

