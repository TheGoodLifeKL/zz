# coding:utf-8

import requests

params = input("请输入要查找的贴吧名字:")

url = 'https://tieba.baidu.com/f?kw={}'.format(params)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}

for n in range(0,10):
    url = url + 'pn=n*50'
    response = requests.get(url=url, headers=headers)
    file_name = '%s-page-%s.html' % (params, (n+1))
    with open(file_name, 'wb') as f:
        f.write(response.content)
        print(file_name)
