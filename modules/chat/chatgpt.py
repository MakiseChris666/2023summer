import openai
import os

os.environ['OPENAI_API_KEY'] = '*'
_char = ['user', 'assistant']

def uploadMsg(msg, model = 'gpt-3.5-turbo'):
    os.environ['OPENAI_API_KEY'] = '*'
    openai.api_key = '*'
    regularized = []
    for i, m in enumerate(msg):
        regularized.append({
            'role': _char[i % 2],
            'content': m
        })
    print(regularized)
    res = openai.ChatCompletion.create(
        model = model,
        messages = regularized
    )
    print(res)
    return res['choices'][0]['message']['content']
