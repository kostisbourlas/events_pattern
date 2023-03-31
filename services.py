from events import publish_event
from repositories import insert_user_in_db
import enums


def send_verification_email():
    print(f"Sent user verification email.")


def send_verification_sms():
    print(f"Sent user verification SMS.")


def register_new_user():
    insert_user_in_db()

    publish_event(enums.EventType.USER_REGISTERED.value)
