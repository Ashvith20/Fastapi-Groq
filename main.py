from fastapi import FastAPI
from groq_client.client import generate_text
from api.routes import router  # Only import the router

app = FastAPI(title="FastAPI OpenAI app")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "FastAPI OpenAI app is running!"}
