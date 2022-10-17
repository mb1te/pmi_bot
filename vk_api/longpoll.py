import aiohttp

from enums import ApiEndpoints
from settings import settings


class LongpollApi:
    KEY: str
    SERVER: str
    TS: str

    async def get_long_poll_url(self):
        params = {
            'access_token': settings.LONG_POLL_ACCESS_TOKEN,
            'group_id': settings.GROUP_ID,
            'v': settings.API_VERSION
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(ApiEndpoints.GET_LONG_POLL_SERVER, params=params) as resp:
                resp = (await resp.json())['response']
                self.KEY = resp.get('key')
                self.SERVER = resp.get('server')
                self.TS = resp.get('ts')

    async def get_updates(self):
        api_url = f'{self.SERVER}?act=a_check&key={self.KEY}&ts={self.TS}&wait=25'
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as resp:
                resp = await resp.json()
                self.TS = resp.get('ts')
                return resp.get('updates')
