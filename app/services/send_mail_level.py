import logging
import requests

from app.core.settings import settings as st
from app.utils.decorator_stmp_exception import smtp_exception_handler
from app.utils.handle_data_email import get_subject_mail, get_body_email
from app.utils.send_mail import SendMail

logging.basicConfig(level=logging.INFO)


class SendMailLevelService:
    mailer: SendMail

    def __init__(self, mailer: SendMail):
        self.base_url = f"{st.url_api}/send_mail"
        self.mailer = mailer

    def send_mail_lv1(self):
        self._send_mail_common(1)

    # def send_mail_lv2(self):
    #     self._send_mail_common(2)
    #
    # def send_mail_lv3(self):
    #     self._send_mail_common(3)

    def send_mail_lv2_3(self):
        self._send_mail_common(2)

    def send_mail_lv4(self):
        self._send_mail_common(4)

    def _send_mail_common(self, level: int):
        params = {"level": level}
        data = self._call_api(params)
        mail_info_list = self._handle_data(data, level)
        self._push_mail_for_level(mail_info_list)

    def _push_mail_for_level(self, mail_list):
        for mail_info in mail_list:
            self._send_bulk_email(mail_info["subject"], mail_info["body"], mail_info["emails"])

    @smtp_exception_handler
    def _call_api(self, params=None):
        url = self.base_url
        try:
            response = requests.get(url, params=params)
            logging.info("Response: %s", response.json())
            return response.json()
        except Exception as e:
            logging.error("Error calling API: %s", e)
            return None

    @smtp_exception_handler
    def _handle_data(self, result, level):
        """
        Process the API response to generate a list of email information for each area.
        Returns a list of dictionaries, where each dictionary contains:
          - subject: Email subject for that area.
          - body: Email content summarizing the total_events.
          - emails: List of recipient emails for that area.
        Areas with no users or valid email addresses are skipped.
        """
        if result is None:
            return []

        mail_info_list = []
        tenants = result.get("data", [])
        for tenant in tenants:
            mail_info_list.extend(self._process_tenant(tenant, level))
        return mail_info_list

    def _process_tenant(self, tenant, level):
        """
        Process data for a single tenant.
        Returns a list of mail_info dictionaries for each valid area under the tenant.
        """
        areas = tenant.get("areas", [])
        tenant_mail_info = []

        for area in areas:
            area_info = self._process_area(area, level)
            if area_info:
                tenant_mail_info.append(area_info)
        return tenant_mail_info

    @staticmethod
    def _process_area(area, level):
        """
        Process a single area under a tenant.
        Returns a mail_info dictionary if the area has valid users with emails;
        otherwise, returns None.
        """

        area_id = area.get("area")
        total_events_pending = area.get("total_events", 0)
        total_pending_event_previous = area.get("pending_event_previous", 0)
        type_of_work = area.get("type_of_work", "")
        users = area.get("users", [])
        if not users:
            logging.info("Area %s: no users, skipping.", area_id)
            return None

        # Retrieve valid email addresses from users
        emails = [user.get("email") for user in users if user.get("email")]
        if not emails:
            logging.info("Area %s: no valid emails, skipping.", area_id)
            return None

        subject = get_subject_mail(level)
        body = get_body_email(level, total_events_pending, total_pending_event_previous, type_of_work)
        logging.info(f"Area: {area_id} with email {emails}")

        return dict(subject=subject, body=body, emails=emails)

    @smtp_exception_handler
    def _send_individual_email(self, subject, body, recipient):
        logging.info("Sending individual email to %s with subject '%s'", recipient, subject)
        self.mailer.send_individual_email(subject, body, recipient)

    @smtp_exception_handler
    def _send_bulk_email(self, subject, body, recipient_list):
        logging.info("Sending bulk email to %s with subject '%s'", recipient_list, subject)
        self.mailer.send_bulk_email(subject, body, recipient_list)

# if __name__ == '__main__':
#     send_mail = SendMail()
#     service = SendMailLevelService(send_mail)
#     service.send_mail_lv1()
#     service.send_mail_lv2()
#     service.send_mail_lv3()
#     service.send_mail_lv4()
#     send_mail.close_connection()
