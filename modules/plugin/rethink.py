import requests
import json

url = "https://api.tigerbot.com/bot-service/plugin/custom/rethink"
API_KEY = '961e87a33df923f0eeea7a865e0c06eac71f99e8cc2ff7577f5b8ec5073e63a3'
headers = {
  'Authorization': 'Bearer ' + API_KEY
}

rethinks: list[dict] = []
curRethink = -1

def createRethink(filepath):
    for r in rethinks:
        if r['name'] == filepath:
            return False, '文件已存在'

    payload = {
        'name': filepath
    }

    url = "https://api.tigerbot.com/bot-service/plugin/custom/create_plugin"
    res = requests.post(url, headers = headers, json = payload)
    resjson = json.loads(res.text)
    if resjson['code'] != 200:
        return False, '创建外部数据库失败'
    pluginID = resjson['data']['pluginId']
    payload = {
        'pluginId': pluginID
    }

    file = open(filepath, 'rb')
    data = {
        'file': file
    }

    url = "https://api.tigerbot.com/bot-service/plugin/custom/add_dataset"
    res = requests.post(url, headers = headers, data = payload, files = data)
    file.close()
    resjson = json.loads(res.text)
    if resjson['code'] != 200:
        return False, '创建外部数据库失败'

    rethinks.append({
        'name': filepath,
        'pluginId': pluginID
    })

    return True, '创建成功'

def delRethink(index):
    url = "https://api.tigerbot.com/bot-service/plugin/custom/del_index"

    headers = {
        'Authorization': 'Bearer ' + API_KEY
    }
    payload = {
        'pluginIds': [rethinks[index]['pluginId']]
    }

    res = requests.post(url, headers = headers, json = payload)

    rethinks.pop(index)

def getRethinkList():
    global rethinks
    url = "https://api.tigerbot.com/bot-service/plugin/custom/get_user_plugin_list"
    payload = {
        'pageNum': 1,
        'pageSize': 1
    }

    res = requests.post(url, headers = headers, json = payload)
    resjson = json.loads(res.text)
    if len(resjson['data']['list']) == 0:
        return
    if resjson['data']['hasMore']:
        payload = {
            'pageNum': 1,
            'pageSize': resjson['data']['total']
        }
        res = requests.post(url, headers = headers, json = payload)
        resjson = json.loads(res.text)
    rethinks = resjson['data']['list']

def uploadRethink(msg, prefix = '请根据上文回答：'):
    payload = {
        'pluginId': rethinks[curRethink]['pluginId'],
        'text': msg,
        'stopOnEmptyData': False,
        'config': {
            'showSearchResult': True,
            'searchResultNum': 6,
            'promptPrefix': prefix,
            'scoreRatio': {
                'tfidf': 0.2,
                'vector': 0.8
            }
        }
    }

    print(prefix)

    res = requests.post(url, headers = headers, json = payload)
    resjson = json.loads(res.text)
    print(res.text)

    ans = resjson['data']['result'][0]
    print(ans)
    return ans

def searchRethink(msg):
    payload = {
        'pluginId': rethinks[curRethink]['pluginId'],
        'text': msg,
        'stopOnEmptyData': False,
        'config': {
            'showSearchResult': True,
            'searchResultNum': 6,
            'promptPrefix': '',
            'scoreRatio': {
                'tfidf': 0.2,
                'vector': 0.8
            }
        }
    }

    res = requests.post(url, headers = headers, json = payload)
    resjson = json.loads(res.text)
    print(res.text)

    ans = resjson['data']['searchResult']
    print(ans)
    return ans