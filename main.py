import requests
import config

def send_message(params):
    proxies = {proxy_type : proxy_url}
    telegram_send_message = telegram_url + bot_token + '/sendMessage'
    r = requests.get(telegram_send_message, params=params, proxies=proxies)

chat_id = int(config.get_param('chat_id'))
telegram_url = config.get_param('telegram_url')
bot_token = config.get_param('bot_token')
proxy_type = config.get_param('proxy_type')
proxy_url = config.get_param('proxy_url')

print(chat_id)
print(telegram_url)
print(bot_token)
print(proxy_type)
print(proxy_url)

if chat_id == 0:
    exit(-1)

test_mess = 'лол-кек-чебурек'
message_params = {
    'chat_id': str(chat_id),
    'text': test_mess}
send_message(message_params)