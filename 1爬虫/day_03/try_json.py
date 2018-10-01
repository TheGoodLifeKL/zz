# coding:utf-8
import requests
import json
from parse_url import parse_url
from pprint import pprint
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
    "Referer":"https://m.douban.com/movie/nowintheater?loc_id=108288"
}

# url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&callback=jsonp1&start=0&count=18&loc_id=108288&_=0"
url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=0"

response = requests.get(url,headers=headers)
# print(response)
html_str = response.content.decode()
# print(html_str)
ret = json.loads(html_str)
pprint(ret)
print(type(ret))

# json.dumps能把python类型转化为json字符串
with open("douban.json","w",encoding="utf-8") as f:
    f.write(json.dumps(ret,ensure_ascii=False,indent=2))

# with open("douban.json","r",encoding="utf-8") as f:
#     ret2 = f.read()
#     ret3 = json.loads(ret2)
#     print(ret3)
#     print(type(ret3))

# 使用json.load提取文件对象中的数据
with open("douban.json","r",encoding="utf-8") as f:
    ret4 = json.load(f)
    print(ret4)
    print(type(ret4))

# json.dump能够把python类型放入类文件对象中
with open("douban1.json","w",encoding="utf-8") as f:
    json.dump(ret,f,ensure_ascii=False,indent=2)






