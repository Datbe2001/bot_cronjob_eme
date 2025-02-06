from contextlib import contextmanager

from app.utils.send_mail import SendMail


@contextmanager
def get_mailer():
    mailer = SendMail()
    try:
        yield mailer
    finally:
        mailer.close_connection()
