import logging
import requests

from config import settings
from enums import ApiEndpoints

logger = logging.getLogger(__name__)


class LongpollApi:
    KEY: str
    SERVER: str
    TS: str

    def __init__(self):
        self.get_long_poll_url()

    def get_long_poll_url(self):
        params = {
            'access_token': settings.LONG_POLL_ACCESS_TOKEN,
            'group_id': settings.GROUP_ID,
            'v': settings.API_VERSION
        }

        response = requests.get(ApiEndpoints.GET_LONG_POLL_SERVER, params=params)
        
        try:
            response.raise_for_status()
        except Exception as e:
            logger.exception(e)
            return

        jsonized = response.json()

        self.KEY = jsonized['response']['key']
        self.SERVER = jsonized['response']['server']
        self.TS = jsonized['response']['ts']

    def get_updates(self):
        api_url = f'{self.SERVER}?act=a_check&key={self.KEY}&ts={self.TS}&wait=25'
        response = requests.get(api_url)
        try:
            response.raise_for_status()
        except Exception as e:
            logger.exception(e)
            return None

        jsonized = response.json()
        
        if ts := jsonized.get('ts'):
            self.TS = ts
            return jsonized['updates']
        
        return None

    def updates(self):
        while True:
            yield from self.get_updates()
