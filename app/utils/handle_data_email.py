from app.templates.template_mail_level_1 import template_mail_lv_1
from app.templates.template_mail_level_2_3 import template_mail_lv_2_3
from app.templates.template_mail_level_4 import template_mail_lv_4


def get_subject_mail(level: int):
    subjects = {
        1: "⏳ Reminder: Complete Your Pending Events Before Your Next Shift!",
        **dict.fromkeys([2, 3], "📌 Daily Reminder: Pending Events for Your Review"),
        4: "📊 Weekly Reminder: Pending Events for Review & Approval"
    }
    return subjects.get(level)


def get_body_email(level: int, pending_event, pending_event_previous, this_shift):
    template_map = {
        1: template_mail_lv_1,
        2: template_mail_lv_2_3,
        3: template_mail_lv_2_3,
        4: template_mail_lv_4
    }
    template_func = template_map.get(level)
    return template_func(pending_event, pending_event_previous, this_shift)
