from celery.schedules import crontab

BEAT_SCHEDULE = {
    'call-api-at-midnight': {
        'task': 'app.services.cron_job.CronJobService.call_api',
        'schedule': crontab(hour=0, minute=0)
    },
    'send-mail-lv1': {
        'task': 'app.services.cron_job.CronJobService.call_send_mail_lv1',
        'schedule': crontab(hour='5,13,22', minute=45),
    },
    'send-mail-lv2': {
        'task': 'app.services.cron_job.CronJobService.call_send_mail_lv2_3',
        'schedule': crontab(hour=7, minute=45),
    },
    'send-mail-lv4': {
        'task': 'app.services.cron_job.CronJobService.call_send_mail_lv_4',
        'schedule': crontab(hour=7, minute=45, day_of_week='monday'),
    },
}
