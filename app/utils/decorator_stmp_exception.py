import logging
import smtplib


def smtp_exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except smtplib.SMTPException as e:
            logging.error(
                "SMTPException encountered in '%s': %s", func.__name__, e, exc_info=True
            )
        except Exception as e:
            logging.error(
                "Unexpected error in '%s': %s", func.__name__, e, exc_info=True
            )

    return wrapper
