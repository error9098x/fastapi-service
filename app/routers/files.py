from fastapi import APIRouter
import json

router = APIRouter()

# Vulnerability 5: Path traversal
@router.get("/files/{filename}")
async def get_file(filename: str):
    with open(f"/uploads/{filename}", 'r') as f:
        content = f.read()
    return {"content": content}

@router.post("/load")
async def load_data(data: str):
    obj = json.loads(data)
    return {"loaded": str(obj)}
