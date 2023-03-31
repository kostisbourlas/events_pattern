from events import map_event
from services import send_verification_email
import enums


def handle_user_registered_event():
    send_verification_email()


def setup_email_event_handlers():
    map_event(
        enums.EventType.USER_REGISTERED.value, handle_user_registered_event
    )
