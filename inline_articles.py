import json
import main_functions


# https://core.telegram.org/bots/api#answerinlinequery
def inline_proposal(query_id, query=''):
    result_article1 = {
        'type': 'article',
        'id': 'article1',
        'title': 'Option number 1',
        'input_message_content': {'message_text': 'This is the first option',}
    }
    result_article2 = {
        'type': 'article',
        'id': 'article2',
        'title': 'Option number 2',
        'input_message_content': {'message_text': 'This is the second option', }
    }
    result_article3 = {
        'type': 'article',
        'id': 'article3',
        'title': 'Option number 3',
        'input_message_content': {'message_text': 'This is the third option', }
    }
    if '1' in query:
        inline_articles = [result_article1,]
    elif '2' in query:
        inline_articles = [result_article2, ]
    elif '3' in query:
        inline_articles = [result_article3, ]
    else:
        inline_articles = [result_article1, result_article2, result_article3]
    inline_query = {
        'inline_query_id': query_id,
        'results': json.dumps(inline_articles)
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
        inline_query = answer['result'][i]['inline_query']['query']
        print('id =', answer['result'][i]['inline_query']['id'])
        print('query =', answer['result'][i]['inline_query']['query'])
        inline_proposal(inline_id, inline_query)
