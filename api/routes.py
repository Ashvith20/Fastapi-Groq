from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from groq_client.client import generate_text

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate_endpoint(request: PromptRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")

    result = generate_text(request.prompt)

    if result.startswith("Error:"):
        raise HTTPException(status_code=500, detail=result)

    return {"response": result}
