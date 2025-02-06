import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.settings import settings as st
from app.utils.decorator_stmp_exception import smtp_exception_handler


class SendMail:
    def __init__(self):
        self.email_host = st.email_host
        self.email_port = st.email_port
        self.email_host_user = st.email_host_user
        self.email_host_password = st.email_host_password
        self.server = None

        try:
            self.server = smtplib.SMTP(self.email_host, self.email_port)
            self.server.starttls()
            self.server.login(self.email_host_user, self.email_host_password)
            logging.info("Successfully connected to SMTP server")
        except smtplib.SMTPException as e:
            logging.error("SMTP error occurred: %s", e)
        except Exception as e:
            logging.error("Error while connecting to SMTP server: %s", e)

    def _compose_email_message(self, subject, body, recipient):
        msg = MIMEMultipart()
        msg['From'] = self.email_host_user
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        return msg

    @smtp_exception_handler
    def send_individual_email(self, subject, body, recipient):
        if not self.server:
            logging.error("SMTP server connection is not available for sending an individual email.")
            return
        msg = self._compose_email_message(subject, body, recipient)
        self.server.send_message(msg)
        logging.info("Individual email sent successfully to '%s'", recipient)

    @smtp_exception_handler
    def send_bulk_email(self, subject, body, recipient_list):
        if not self.server:
            logging.error("SMTP server connection is not available for sending bulk emails.")
            return
        recipients = ", ".join(recipient_list)
        msg = self._compose_email_message(subject, body, recipients)
        self.server.sendmail(self.email_host_user, recipient_list, msg.as_string())
        logging.info("Bulk email sent successfully to recipients: %s", recipients)

    @smtp_exception_handler
    def close_connection(self):
        if not self.server:
            logging.error("SMTP server connection is not available to close.")
            return
        self.server.quit()
        logging.info("SMTP server connection closed successfully.")
