# coding:utf-8
import requests

headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
# p = {"wd":"传智播客"}
# url_temp = "https://www.baidu.com/s?"
#
# r = requests.get(url_temp,headers=headers,params=p)
# print(r.status_code)
# print(r.request.url)

url = "https://www.baidu.com/s?wd={}".format("传智播客")
r = requests.get(url,headers=headers)
print(r.status_code)
print(r.url)