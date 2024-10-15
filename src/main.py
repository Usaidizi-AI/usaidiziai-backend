from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.auth.router import auth_router

app = FastAPI(title="Learnit Backend API routes", docs_url="/")

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_credentials=True,
        allow_headers=["*"]
        )

app.include_router(auth_router, prefix="/api/v1", tags=["User Authentication routes"])
