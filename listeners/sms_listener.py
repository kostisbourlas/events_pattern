from events import map_event
from services import send_verification_sms
import enums


def handle_user_registered_event():
    send_verification_sms()


def setup_sms_event_handlers():
    map_event(
        enums.EventType.USER_REGISTERED.value, handle_user_registered_event
    )