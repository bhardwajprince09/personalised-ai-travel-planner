# backend/app/main.py (top imports)
import os
from fastapi.middleware.cors import CORSMiddleware

FRONTEND_URL = os.getenv("FRONTEND_URL", "*")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL] if FRONTEND_URL != "*" else ["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

