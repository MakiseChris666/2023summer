import requests
import json

API_KEY = '961e87a33df923f0eeea7a865e0c06eac71f99e8cc2ff7577f5b8ec5073e63a3'
url = "https://api.tigerbot.com/bot-service/ai_service/gpt"
headers = {
  'Authorization': 'Bearer ' + API_KEY
}

commonInsturction = '上文是一段对话，其中用户的问题带有“User:”前缀，机器给出的回答带有“Bot:”前缀。现在，请你以机器的身份回答以下问题，\
注意不要重复上文，也不要加上前缀：\n'

def uploadMsg(hist, message, instruction = commonInsturction):
    if hist == '':
        payload = {
            'text': message
        }
    else:
        payload = {
            'text': hist + instruction + message
        }
    print(payload['text'])
    res = requests.post(url, headers = headers, json = payload)
    resjson = json.loads(res.text)
    print(res.text)

    ans = resjson['data']['result'][0]
    return ans

if __name__ == '__main__':
    res = uploadMsg('', '你好')
    print(res)