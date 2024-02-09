
API_KEY = '961e87a33df923f0eeea7a865e0c06eac71f99e8cc2ff7577f5b8ec5073e63a3'
# import requests
#
# url = "https://api.tigerbot.com/bot-service/ft/upload_train_data"
#
# headers = {
#   'Authorization': 'Bearer ' + API_KEY
# }
#
# your_json_file_path = './external/luxun2.json'
#
# files = {'file': open(your_json_file_path, 'rb')}
#
# response = requests.post(url, headers=headers, files=files)
#
# print(response.text)

# import requests
#
# url = "https://api.tigerbot.com/bot-service/ft/start_train"
#
# headers = {
#   'Authorization': 'Bearer ' + API_KEY
# }
#
# payload = {
#   'ftId': 'ft5490'
# }
#
# response = requests.post(url, headers=headers, json=payload)
#
# print(response.text)

# import requests
#
# url = "https://api.tigerbot.com/bot-service/ft/get_fine_tune_list"
#
# headers = {
#   'Authorization': 'Bearer ' + API_KEY
# }
#
# payload = {
#   # 'ftId': 'ft5490',
#   'pageNum': 1,
#   'pageSize': 5
# }
#
# response = requests.post(url, headers=headers, json=payload)
#
# print(response.text)

import requests

url = "https://api.tigerbot.com/bot-service/ft/online"

headers = {
  'Authorization': 'Bearer ' + API_KEY
}

payload = {
  'ftId': 'ft5490'
}

response = requests.post(url, headers=headers, json=payload)

print(response.text)

