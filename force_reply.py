import json
import config
import main_functions

chat_id = config.get_param('chat_id')
print(chat_id)
if chat_id == '0':
    exit(-1)

test_mess = 'Please respond the message'

# https://core.telegram.org/bots/api#deletemessage
# https://core.telegram.org/bots/api#forcereply
force_reply = {'force_reply': True,}
message_params_force_reply = {
    'chat_id': chat_id,
    'text': test_mess,
    'reply_markup': json.dumps(force_reply)}
answer = main_functions.send_message(message_params_force_reply)
print(answer.text)
