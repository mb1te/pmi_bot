from command_processing.handler import Handler
from vk_api.longpoll import LongpollApi

if __name__ == '__main__':
    client = LongpollApi()

    for update in client.updates():
        print(update)
        Handler.answer(update)
