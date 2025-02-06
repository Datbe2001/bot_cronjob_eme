import unittest
from unittest.mock import patch, MagicMock
import logging

from app.utils.send_mail import SendMail


class TestSendMail(unittest.TestCase):

    @patch('send_mail.smtplib.SMTP')
    def test_send_individual_email(self, mock_smtp):
        # Thiết lập mock cho SMTP instance
        smtp_instance = mock_smtp.return_value
        smtp_instance.send_message = MagicMock()

        # Khởi tạo SendMail, quá trình kết nối sẽ dùng mock
        mailer = SendMail()

        subject = "Test Subject"
        body = "<p>This is a test email</p>"
        recipient = "datbe26092001@gmail.com"
        mailer.send_individual_email(subject, body, recipient)

        # Kiểm tra xem send_message đã được gọi chưa
        smtp_instance.send_message.assert_called_once()
        logging.info("test_send_individual_email passed")

    @patch('send_mail.smtplib.SMTP')
    def test_send_bulk_email(self, mock_smtp):
        smtp_instance = mock_smtp.return_value
        smtp_instance.sendmail = MagicMock()

        mailer = SendMail()

        subject = "Bulk Test Subject"
        body = "<p>This is a bulk test email</p>"
        recipients = ["test1@example.com", "test2@example.com"]
        mailer.send_bulk_email(subject, body, recipients)

        # Kiểm tra xem sendmail đã được gọi chưa
        smtp_instance.sendmail.assert_called_once()
        logging.info("test_send_bulk_email passed")

    @patch('send_mail.smtplib.SMTP')
    def test_close_connection(self, mock_smtp):
        smtp_instance = mock_smtp.return_value
        smtp_instance.quit = MagicMock()

        mailer = SendMail()
        mailer.close_connection()

        # Kiểm tra xem quit đã được gọi chưa
        smtp_instance.quit.assert_called_once()
        logging.info("test_close_connection passed")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
