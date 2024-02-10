
API_KEY = '*'
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

