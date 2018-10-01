# coding:utf-8
import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}



@retry(stop_max_attempt_number=3)
def _parse_url(url,method,data):
    print("*"*20)
    if method == "POST":
        response = requests.post(url,data=data,headers=headers)
    else:
        response = requests.get(url,headers=headers,timeout=3)
    assert response.status_code == 200
    return response.content.decode()

def parse_url(url,method="GET",data=None):
    try:
        html_str = _parse_url(url,method,data)
    except:
        html_str = None

    return html_str

if __name__ == '__main__':
    url = "https://www.baidu.com"
    print(parse_url(url))