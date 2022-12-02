__all__ = ['send_message']
from .messages import *


def send_message(message_key):
    print(all_messages_text[message_key])
