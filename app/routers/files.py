from fastapi import APIRouter
import pickle

router = APIRouter()

# Vulnerability 5: Path traversal
@router.get("/files/{filename}")
async def get_file(filename: str):
    with open(f"/uploads/{filename}", 'r') as f:
        content = f.read()
    return {"content": content}

# Vulnerability 6: Insecure deserialization
@router.post("/load")
async def load_data(data: str):
    obj = pickle.loads(data.encode('latin1'))
    return {"loaded": str(obj)}
