from celery import Celery

from app.core.settings import settings as st
from app.gateway.celery_beats import BEAT_SCHEDULE


class CeleryWorker:
    def __init__(self):
        self.celery = Celery(
            "worker",
            broker=f"redis://{st.redis_host}:{st.redis_port}/0",
            backend=f"redis://{st.redis_host}:{st.redis_port}/0"
        )
        self.celery.conf.beat_schedule = BEAT_SCHEDULE
        self.celery.autodiscover_tasks(['app.services'])
        self.celery.conf.broker_connection_retry_on_startup = True


celery_instance = CeleryWorker().celery

