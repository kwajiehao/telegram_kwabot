"""simple Telegram bot"""
# hackermoon telegram bot tutorial
# https://hackernoon.com/how-to-create-and-deploy-a-telegram-bot-2addd8aec6b4

########## Part 1

import datetime
import requests
from time import sleep

class BotHandler:
    """My telegram bot"""
    def __init__(self, token):
        """Initiate class"""
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        """Get updates for bot"""
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        """Sends message to bot"""
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        """Gets update from bot"""
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update

GREET_BOT = BotHandler(token)
GREETINGS = ('hello', 'hi', 'greetings', 'sup')
NOW = datetime.datetime.now()

def main():
    """Main method"""
    new_offset = None
    today = NOW.day
    hour = NOW.hour

    while True:
        GREET_BOT.get_updates(new_offset)

    last_update = GREET_BOT.get_last_update()
    last_update_id = last_update['update_id']

    last_chat_text = last_update['message']['text']
    last_chat_id = last_update['message']['chat']['id']
    last_chat_name = last_update['message']['chat']['first_name']

    if last_chat_text.lower() in GREETINGS and today == NOW.day and 6 <= hour < 12:
        GREET_BOT.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
        today += 1

    elif last_chat_text.lower() in GREETINGS and today == NOW.day and 12 <= hour < 17:
        GREET_BOT.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
        today += 1

    elif last_chat_text.lower() in GREETINGS and today == NOW.day and 17 <= hour < 23:
        GREET_BOT.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
        today += 1

    new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
