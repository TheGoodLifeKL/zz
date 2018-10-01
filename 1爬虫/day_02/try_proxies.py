# coding:utf-8

import requests

# proxies = {"http":"http://101.96.11.39:8080"}
proxies = {"http":"http://101.236.35.98:8866"}
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
reponse = requests.get("http://www.baidu.com",proxies=proxies,headers=headers)
# print(reponse.content.decode())
print(reponse.status_code)

