import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.route import route
from app.core.settings import settings as st

app = FastAPI(title="Bot Cron Job EmagicEyes", version="1.1.1")
logging.basicConfig(level=logging.INFO)

app.include_router(route, prefix="")

app.add_middleware(
    CORSMiddleware,
    allow_origins=st.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", reload=True)
