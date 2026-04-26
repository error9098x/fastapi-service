from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import hashlib

app = FastAPI()

# Vulnerability 1: CORS misconfiguration - allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Vulnerability 2: SQL Injection
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return {"user": result}

# Vulnerability 3: Missing authentication on admin endpoint
@app.delete("/admin/users/{user_id}")
async def delete_user(user_id: int):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()
    conn.close()
    return {"message": "User deleted"}

# Vulnerability 4: Weak cryptography - MD5
@app.post("/hash")
async def hash_password(password: str):
    hashed = hashlib.md5(password.encode()).hexdigest()
    return {"hash": hashed}
