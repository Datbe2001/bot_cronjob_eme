import logging

import requests
from fastapi import HTTPException

from app.constant.app_status import AppStatus
from app.gateway.celery_worker import celery_instance
from app.gateway.contextmanager_stmp import get_mailer
from app.services.send_mail_level import SendMailLevelService
from app.utils.send_mail import SendMail

logger = logging.getLogger(__name__)


class CronJobService:

    @staticmethod
    @celery_instance.task(name='app.services.cron_job.CronJobService.call_api')
    def call_api():
        try:
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            logging.info("Call successfully.")
            return response.json()
        except HTTPException:
            raise HTTPException(**AppStatus.ERROR_INTERNAL_SERVER_ERROR.meta)

    @staticmethod
    @celery_instance.task(name='app.services.cron_job.CronJobService.call_send_mail_lv1')
    def call_send_mail_lv_1():
        with get_mailer() as mailer:
            send_mail_service = SendMailLevelService(mailer)
            result = send_mail_service.send_mail_lv1()
            return result

    @staticmethod
    @celery_instance.task(name='app.services.cron_job.CronJobService.call_send_mail_lv2_3')
    def call_send_mail_lv2_3():
        with get_mailer() as mailer:
            send_mail_service = SendMailLevelService(mailer)
            result = send_mail_service.send_mail_lv2_3()
            return result

    @staticmethod
    @celery_instance.task(name='app.services.cron_job.CronJobService.call_send_mail_lv_4')
    def call_send_mail_lv_4():
        with get_mailer() as mailer:
            send_mail_service = SendMailLevelService(mailer)
            result = send_mail_service.send_mail_lv4()
            return result


cron_job_service = CronJobService()
