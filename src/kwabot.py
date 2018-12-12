"""simple Telegram bot"""
# hackermoon telegram bot tutorial
# https://hackernoon.com/how-to-create-and-deploy-a-telegram-bot-2addd8aec6b4

########## Part 1

imer datetime
from argparse import ArgumentParserow ow to 
import requests


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


def main():
    """Main method"""

    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


    parser = ArgumentParser('Token ID to be passed here')
    parser.add_argument('--token', type=str, required=True, dest='token')
    args = parser.parse_args()

    greet_bot = BotHandler(args.token)
    greetings = ('hello', 'hi', 'greetings', 'sup')
    now = datetime.datetime.now()

    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

    last_update = greet_bot.get_last_update()
    last_update_id = last_update['update_id']

    last_chat_text = last_update['message']['text']
    last_chat_id = last_update['message']['chat']['id']
    last_chat_name = last_update['message']['chat']['first_name']

    if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
        greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
        today += 1

    elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
        greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
        today += 1

    elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
        greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
        today += 1

    new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
