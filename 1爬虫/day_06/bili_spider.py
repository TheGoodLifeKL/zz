# coding:utf-8
import requests
import re

class BiLiSpider:
    def __init__(self):
        self.url_temp = 
        self.url = "https://www.bilibili.com/video/av26364088/"
        self.danmu_url = "https://api.bilibili.com/x/v1/dm/list.so?oid={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
        }


    def get_html(self):
        response = requests.get(self.url,headers=self.headers)
        return response.content.decode()


    def run(self):
        # 获取url,发送请求,获取响应
        html = self.get_html()
        # 提取弹幕url的oid
        re.findall(r"<option value='.*?' cid=(d\+)'>",html)
        if



