import pytest
from httpx import AsyncClient
from app.main import app

AUTH_HEADER = {"Authorization": "Bearer testtoken"}

@pytest.mark.asyncio
async def test_create_and_get_chat():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create chat
        response = await ac.post("/api/v1/chats/create-chat", json={"name": "Test Chat"}, headers=AUTH_HEADER)
        assert response.status_code == 200
        data = response.json()
        chat_id = data["chat_id"]

        # Get chat
        response = await ac.get(f"/api/v1/chats/get-chat?chat_id={chat_id}", headers=AUTH_HEADER)
        assert response.status_code == 200
        chat = response.json()
        assert chat["chat_id"] == chat_id
        assert chat["name"] == "Test Chat"

@pytest.mark.asyncio
async def test_add_message():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create chat
        response = await ac.post("/api/v1/chats/create-chat", json={"name": "Chat for Msg"}, headers=AUTH_HEADER)
        chat_id = response.json()["chat_id"]

        # Add message
        msg_payload = {
            "chat_id": chat_id,
            "question": "Hi",
            "response": "Hello!"
        }
        response = await ac.post("/api/v1/messages/add-message", json=msg_payload, headers=AUTH_HEADER)
        assert response.status_code == 200
        message = response.json()
        assert message["question"] == "Hi"
        assert message["response"] == "Hello!"

@pytest.mark.asyncio
async def test_create_branch():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create chat and add a message
        chat_resp = await ac.post("/api/v1/chats/create-chat", json={"name": "Parent Chat"}, headers=AUTH_HEADER)
        chat_id = chat_resp.json()["chat_id"]
        await ac.post("/api/v1/messages/add-message", json={"chat_id": chat_id, "question": "Q1", "response": "R1"}, headers=AUTH_HEADER)

        # Create branch from first message (index 0)
        branch_payload = {
            "parent_chat_id": chat_id,
            "message_index": 0,
            "name": "Branch Chat"
        }
        response = await ac.post("/api/v1/branches/create-branch", json=branch_payload, headers=AUTH_HEADER)
        assert response.status_code == 200
        branch_chat = response.json()
        assert branch_chat["name"] == "Branch Chat"
