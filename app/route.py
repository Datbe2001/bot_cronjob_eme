from fastapi import APIRouter

from app.endpoint import cron_job

route = APIRouter()

route.include_router(cron_job.router, tags=["Cron Job"])
