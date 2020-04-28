import json
import config
import main_functions



chat_id = config.get_param('chat_id')
print(chat_id)
if chat_id == '0':
    exit(-1)

test_mess = config.get_param('sample_text')

# ******************************************************
key1 = {'text': 'key1',
        'callback_data': 'key1'}
key2 = {'text': 'key2',
        'callback_data': 'key2'}
key3 = {'text': 'key3',
        'callback_data': 'key3'}
key4 = {'text': 'key4',
        'callback_data': 'key4'}
key_switch = {'text': 'switch_key',
            'switch_inline_query_current_chat': 'some query'}
key_row1 = [key1, key2]
key_row2 = [key3, key4]
key_row3 = [key_switch,]
inline_keyboard_markup = {'inline_keyboard': [key_row1, key_row2, key_row3]}
inline_keyboard_markup2 = {'inline_keyboard': [key_row2, key_row1]}
# https://core.telegram.org/bots/api#inlinekeyboardmarkup
# ******************************************************

print(json.dumps(inline_keyboard_markup))
message_params_inline = {
    'chat_id': chat_id,
    'text': test_mess,
    'reply_markup': json.dumps(inline_keyboard_markup)}
# send message with inline keyboard and get message_id
# message_id is needed to update message (change inline keyboard)
answer = main_functions.send_message(message_params_inline)
data = json.loads(answer.text)
mess_id = data['result']['message_id']

# wait for user answer
str = input('Do the next step?')

# change inline keyboard of existing message
message_params_edit = {
    'chat_id': chat_id,
    'message_id': mess_id,
    'reply_markup': json.dumps(inline_keyboard_markup2)}
main_functions.update_message(message_params_edit)
