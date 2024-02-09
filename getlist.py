import requests
import json

API_KEY = '9f09747e404a476325a17d13f76302ca447ab4b0f50e5221aaf967dcd2b17871'
url = "https://api.tigerbot.com/bot-service/plugin/custom/get_user_plugin_list"

headers = {
  'Authorization': 'Bearer ' + API_KEY
}

payload = {
  'pageNum': 1,
  'pageSize': 1
}

response = requests.post(url, headers=headers, json=payload)

print(response.text)

resjson = json.loads(response.text)
print(resjson['data']['hasMore'])