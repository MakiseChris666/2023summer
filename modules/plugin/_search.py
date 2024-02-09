import requests
from bs4 import BeautifulSoup
import os

def searchBing(question,j=200,index=4):
    """
    question:搜索的问题
    j:限制返回的单条内容的长度的近似值，实际略大于j
    index=搜索内容的条数,超过最大搜索条数时以最大条数为准
    返回值：一个包含搜索内容的列表
    """

    href="https://cn.bing.com/search?q={}".format(question)
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67",
        "referer":"https://ntp.msn.cn/"
    }
    res = requests.get(href, headers=headers, proxies = None)
    soup = BeautifulSoup(res.text,'html.parser')
    titles = soup.select('div#b_content li.b_algo h2')
    contents=soup.select('div#b_content li.b_algo div p')
    title=[titles[i].text for i in range(len(titles))]
    content=[contents[i].text for i in range(len(contents))]
    if index>len(titles):
        index=len(titles)
    res=[]
    for i in range(index):
        s=title[i]+content[i][0:j]
        res.append(s)

    return res

if __name__ == '__main__':
    res = searchBing('北京交通大学')
    for r in res:
        print(len(r))