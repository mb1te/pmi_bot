from enums import UpdateType, UserID
from utils import get_chance
from vk_api.message import MessageApi

class Handler:
    @classmethod
    def answer(cls, update):
        if update['type'] == UpdateType.NEW_MESSAGE:
                message = update['object']['message']
                if message['from_id'] == UserID.KARPAEVA_JULIYA and get_chance(0.1):
                    MessageApi.send_message(
                        peer_id=message['peer_id'],
                        message='@yuliya_karpaeva иди замуж!',
                        forwarded_msg=[message['conversation_message_id']]
                    )
