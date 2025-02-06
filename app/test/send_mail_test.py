import logging

from app.templates.template_mail_level_1 import template_mail_lv_1
from app.utils.send_mail import SendMail


def test_send_email_real(pending_event, pending_event_previous, this_shift, recipient):
    logging.basicConfig(level=logging.INFO)
    mailer = SendMail()
    subject = "Test Email from SendMail Service"

    html_template = template_mail_lv_1(
        pending_event=pending_event,
        pending_event_previous=pending_event_previous,
        this_shift=this_shift
    )

    mailer.send_individual_email(subject, html_template, recipient)
    mailer.close_connection()


if __name__ == '__main__':
    mailer = SendMail()
    subject = "Bulk Email Test"
    body = "This is a test email for multiple recipients."
    recipient_list = ["datbe26092001@gmail.com", "datbe3333@gmail.com"]

    mailer.send_bulk_email(subject, body, recipient_list)
    mailer.close_connection()
