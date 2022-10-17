import json
from random import randint

import aiohttp

from enums import ApiEndpoints
from settings import settings


class MessageApi:
    @classmethod
    async def send_message(cls, peer_id: list[int], message: str, forwarded_msg: list[int] | None) -> None:
        params = {
            'access_token': settings.MESSAGES_ACCESS_TOKEN,
            'peer_id': peer_id,
            'message': message,
            'v': settings.API_VERSION,
            'random_id': randint(0, 2**31)
        }

        if isinstance(forwarded_msg, list):
            jsonized = {
                "peer_id": peer_id,
                "conversation_message_ids": forwarded_msg,
                "is_reply": int(len(forwarded_msg) == 1)
            }
            params['forward'] = json.dumps(jsonized)

        async with aiohttp.ClientSession() as session:
            await session.get(ApiEndpoints.SEND_MESSAGE, params=params)
