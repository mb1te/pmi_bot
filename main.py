import asyncio
import platform
from random import random

from vk_api.longpoll import LongpollApi
from enums import UpdateType, UserID
from vk_api.message import MessageApi


def get_chance(probability: float) -> bool:
    return random() < probability


async def main():
    client = LongpollApi()
    await client.get_long_poll_url()

    while True:
        updates = await client.get_updates()
        for update in updates:
            if update['type'] == UpdateType.NEW_MESSAGE:
                message = update['object']['message']
                if message['from_id'] == UserID.KARPAEVA_JULIYA and get_chance(0.05):
                    await MessageApi.send_message(
                        peer_id=message['peer_id'],
                        message='@yuliya_karpaeva иди замуж!',
                        forwarded_msg=[message['conversation_message_id']]
                    )


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
