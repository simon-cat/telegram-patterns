import json
import main_functions


# https://core.telegram.org/bots/api#answerinlinequery
def inline_proposal(query_id):
    result_contact1 = {
        'type': 'contact',
        'id': 'c1',
        'phone_number': '1',
        'first_name': 'FirstName01',
        'last_name': 'LastName01', }
    result_contact2 = {
        'type': 'contact',
        'id': 'c2',
        'phone_number': '2',
        'first_name': 'FirstName02',
        'last_name': 'LastName02', }
    result_contact3 = {
        'type': 'contact',
        'id': 'c3',
        'phone_number': '3',
        'first_name': 'FirstName03',
        'last_name': 'LastName03', }
    inline_contacts = [result_contact1, result_contact2, result_contact3]
    inline_query = {
        'inline_query_id': query_id,
        'results': json.dumps(inline_contacts)
    }
    answer = main_functions.inline_query(inline_query)
    print(answer)
    print(answer.text)

# getting new messages
update_params = {}
update = main_functions.get_updates(update_params)
answer = json.loads(update.text)
for i in range(len(answer['result'])):
    if 'inline_query' in answer['result'][i]:
        # https://core.telegram.org/bots/api#inlinequery
        inline_id = answer['result'][i]['inline_query']['id']
        print('id =', answer['result'][i]['inline_query']['id'])
        print('query =', answer['result'][i]['inline_query']['query'])
        inline_proposal(inline_id)
