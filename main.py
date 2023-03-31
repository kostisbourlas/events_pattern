from listeners.email_listener import setup_email_event_handlers
from services import register_new_user
from listeners.sms_listener import setup_sms_event_handlers


setup_email_event_handlers()
setup_sms_event_handlers()


if __name__ == "__main__":
    register_new_user()
