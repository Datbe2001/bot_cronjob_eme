import logging

from fastapi import APIRouter

from app.services.cron_job import cron_job_service

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/test-trigger-task")
def trigger_task():
    logger.info("Endpoints: cron_job called.")
    cron_job_service.call_api.delay()
    return {"message": "Trigger task is activated"}


@router.get("/trigger-level-1")
def trigger_task():
    logger.info("Endpoints: Cron job level 1 called.")
    cron_job_service.call_send_mail_lv_1.delay()
    return {"message": "Trigger send mail level 1 is activated"}


@router.get("/trigger-level-2-3")
def trigger_task():
    logger.info("Endpoints: Cron job level 2&3 called.")
    cron_job_service.call_send_mail_lv2_3.delay()
    return {"message": "Trigger send mail level 2&3 is activated"}


@router.get("/trigger-level-4")
def trigger_task():
    logger.info("Endpoints: Cron job level 4 called.")
    cron_job_service.call_send_mail_lv_4.delay()
    return {"message": "Trigger send mail level 4 is activated"}


@router.get("/send_mail")
def trigger_task(level: str):
    return {
        "data": [
            {
                "tenant": 7272152071833559,
                "areas": [
                    {
                        "area": 7272426293566808,
                        "total_events": 21,
                        "pending_event_previous": 21,
                        "type_of_work": "23",
                        "users": [
                            {
                                "id": 72216672326383673,
                                "name": "Dat 1",
                                "email": "datbe26092001@gmail.com"
                            },
                            {
                                "id": 7259142707518546,
                                "name": "QC DCbn",
                                "email": "datbe3333@gmail.com"
                            }
                        ]
                    },
                    {
                        "area": 7272426240013935,
                        "total_events": 73,
                        "pending_event_previous": 123123,
                        "type_of_work": "23",
                        "users": [
                            {
                                "id": 72216672326383673,
                                "name": "Viet",
                                "email": "vietgym007@gmail.com"
                            },
                            {
                                "id": 7259142707518546,
                                "name": "Viet nhoc2k3007",
                                "email": "nhoc2k3007@gmail.com"
                            }
                        ]
                    }
                ],

            },
            {
                "tenant": 7202536272282427,
                "areas": [
                    {
                        "area": 7236746774893994,
                        "total_events": 841,
                        "pending_event_previous": 8341,
                        "type_of_work": "23",
                        "users": [
                            {
                                "id": 7266672326383673,
                                "name": "Khanh",
                                "email": "khanhlq2901@gmail.com"
                            },
                            {
                                "id": 7259142707518546,
                                "name": "Nhan",
                                "email": "nhando393@gmail.com"
                            }
                        ]
                    },
                    {
                        "area": 7234860430563385,
                        "total_events": 37850,
                        "pending_event_previous": 378250,
                        "type_of_work": "23",
                        "users": [
                            {
                                "id": 7266672926060093,
                                "name": "datdev",
                                "email": "datdev.it2609@gmail.com"
                            },
                            {
                                "id": 7266672869617345,
                                "name": "tnhan.ittechnology",
                                "email": "tnhan.ittechnology@gmail.com"
                            },
                            {
                                "id": 7266673012718608,
                                "name": "dothanhnhanbh",
                                "email": "dothanhnhanbh.2001@gmail.com"
                            }
                        ]
                    }
                ],

            }
        ]
    }
