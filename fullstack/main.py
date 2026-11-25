from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from core.database import engine, Base
from core.limiter import limiter
from models import user, note, category  # noqa: F401  (регистрация всех моделей в Base)
from routers import auth, users, notes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Сервис заметок")

# Rate Limiting setup
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS setup
import os as _os

_cors_origins = [o.strip() for o in _os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(notes.router)

@app.get("/")
def read_root():
    return {"message": "Привет, FastAPI! Сервис заметок работает."}