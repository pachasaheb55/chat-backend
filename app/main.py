from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi
from app.routes.chat_route import router
from app.routes import auth_route

security = HTTPBearer()

app = FastAPI(title="FastAPI Chat Application with Branching Functionality ")
app.include_router(router)
app.include_router(auth_route.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Chat API",
        version="1.0.0",
        description="Microservice-based chat backend with branching",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for operation in path.values():
            operation["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

