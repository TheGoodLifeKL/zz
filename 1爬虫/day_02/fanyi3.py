# coding:utf-8
import requests
import json
import sys

query_string = sys.argv[1]
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}

judge_data = {"query":query_string}
judge_language_url = "http://fanyi.baidu.com/langdetect"
judge_response = requests.post(judge_language_url, data=judge_data, headers=headers)
judge_ret_dict = json.loads(judge_response.content.decode())
judge_ret = judge_ret_dict["lan"]

if judge_ret == "zh":

    data = {
        "query": query_string,
        "from": "zh",
        "to": "en",
    }
else:
    data = {
        "query": query_string,
        "from": "en",
        "to": "zh",
    }

print(data)

post_url = "http://fanyi.baidu.com/basetrans"

response = requests.post(post_url,data=data,headers=headers)
# print(response.content.decode())
ret_dict = json.loads(response.content.decode())
ret = ret_dict["trans"][0]["dst"]
print("结果是:",ret)