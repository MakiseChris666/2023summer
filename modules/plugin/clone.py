import requests
import json

API_KEY = '961e87a33df923f0eeea7a865e0c06eac71f99e8cc2ff7577f5b8ec5073e63a3'

def luxunClone(msg):
    url = "https://api.tigerbot.com/bot-service/ft/call"

    headers = {
        'Authorization': 'Bearer ' + API_KEY
    }
    payload = {
        'ftId': 'ft5491',
        'text': '请模仿鲁迅写一段话来回答下面的问题：\n' + msg
    }

    print(payload['text'])
    res = requests.post(url, headers = headers, json = payload)
    resjson = json.loads(res.text)
    print(res.text)

    return resjson['data']['result'][0]

def jhzClone(msg):
    url = "https://api.tigerbot.com/bot-service/ft/call"

    headers = {
        'Authorization': 'Bearer ' + API_KEY
    }
    payload = {
        'ftId': 'ft5490',
        'text': '请为这一句诗续写下一句：' + msg
    }

    print('aaa')
    print(payload['text'])
    res = requests.post(url, headers = headers, json = payload)
    resjson = json.loads(res.text)
    print(res.text)

    return resjson['data']['result'][0]
