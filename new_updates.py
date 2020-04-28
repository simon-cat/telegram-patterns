import json
import main_functions

update_params = {}

# getting new messages
update = main_functions.get_updates(update_params)
answer = json.loads(update.text)
max = 0
for i in range(len(answer['result'])):
    print(answer['result'][i]['update_id'])
    print(answer['result'][i])
    if max < answer['result'][i]['update_id']:
        max = answer['result'][i]['update_id']

# clear queue of messages
update_params['offset'] = max + 1
main_functions.get_updates(update_params)
