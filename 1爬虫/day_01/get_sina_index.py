# coding:utf-8

import requests

response = requests.get('https://www.sina.com.cn/')

with open('index.html','wb') as f:
    f.write(response.content)
