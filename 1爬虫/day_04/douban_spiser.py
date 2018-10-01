# coding:utf-8
import requests
import json
import csv

class DoubanSpider:
    def __init__(self):
        self.url_temp_list = [
            {
                "url_temp":"https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=0",
                "country":"US"
            },
            {
                "url_temp":"https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_english_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=1531389058864",
                "country":"UK"
            },
            {
                "url_temp":"https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_korean_drama_hot/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=1531389131593",
                "country":"kr"
            }
            ]
        self.headers = {
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
            "Referer":"https://m.douban.com/tv/american"
        }
    def parse_url(self,url):
        print(url)
        response = requests.get(url,headers = self.headers)
        return response.content.decode()

    def get_content_list(self,json_str):
        dict_ret = json.loads(json_str)
        print(dict_ret)
        content_list = dict_ret["subject_collection_items"]
        total = dict_ret["total"]
        return content_list,total

    def save_content_list(self,content_list,country):
        with open("douban.csv","a") as f:
            for content in content_list:
                content["country"] = country
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n") # 写入换行符

    def run(self):
        # start_url
        for url_temp in self.url_temp_list:
            num = 0
            total = 100
            while num < total:
                url = url_temp["url_temp"].format(num)
                # 发送请求,获取响应
                json_str = self.parse_url(url)
                print("*"*30)
                print(json_str)
                print("*"*30)
                # 提取数据
                content_list,total = self.get_content_list(json_str)
                # 保存
                self.save_content_list(content_list,url_temp["country"])
                # if len(content_list) < 18:
                #     break
                # 构造下一个url
                num += 18

if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()
