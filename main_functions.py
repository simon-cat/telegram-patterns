import requests
import config

# https://core.telegram.org/bots/api#getupdates
def get_updates(params,\
                 proxy_type=config.get_param('proxy_type'),\
                 proxy_url=config.get_param('proxy_url'),\
                 telegram_url=config.get_param('telegram_url'),\
                 bot_token=config.get_param('bot_token')):
    proxies = {proxy_type: proxy_url}
    telegram_method = telegram_url + bot_token + '/getUpdates'
    print(telegram_method)
    return requests.get(telegram_method, params=params, proxies=proxies)

# https://core.telegram.org/bots/api#inlinequery
def inline_query(params,\
                 proxy_type=config.get_param('proxy_type'),\
                 proxy_url=config.get_param('proxy_url'),\
                 telegram_url=config.get_param('telegram_url'),\
                 bot_token=config.get_param('bot_token')):
    proxies = {proxy_type: proxy_url}
    telegram_method = telegram_url + bot_token + '/answerInlineQuery'
    return requests.get(telegram_method, params=params, proxies=proxies)

# https://core.telegram.org/bots/api#sendmessage
def send_message(params,\
                 proxy_type=config.get_param('proxy_type'),\
                 proxy_url=config.get_param('proxy_url'),\
                 telegram_url=config.get_param('telegram_url'),\
                 bot_token=config.get_param('bot_token')):
    proxies = {proxy_type : proxy_url}
    telegram_method = telegram_url + bot_token + '/sendMessage'
    return requests.get(telegram_method, params=params, proxies=proxies)

# https://core.telegram.org/bots/api#editmessagereplymarkup
def update_message(params,\
                 proxy_type=config.get_param('proxy_type'),\
                 proxy_url=config.get_param('proxy_url'),\
                 telegram_url=config.get_param('telegram_url'),\
                 bot_token=config.get_param('bot_token')):
    proxies = {proxy_type : proxy_url}
    telegram_method = telegram_url + bot_token + '/editMessageReplyMarkup'
    return requests.get(telegram_method, params=params, proxies=proxies)
