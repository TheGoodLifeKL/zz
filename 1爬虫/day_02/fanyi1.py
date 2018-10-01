# coding:utf-8
import requests

headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

data = {
    "from":"en",
    "to":"zh",
    "query":"trust you",
    "transtype":"translang",
    "simple_means_flag":"3",
    "sign":"793832.589785",
    "token":"1775f2d1a429ca5f0a6d2dfb37dbeaf1"
}

post_url = "http://fanyi.baidu.com/v2transapi"

response = requests.post(post_url,data=data,headers=headers)
print(response.content.decode())