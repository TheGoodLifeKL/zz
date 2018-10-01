# coding:utf-8
import requests
from lxml import etree
import json

class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
        }

    def get_url_list(self):
        print("----3----")
        return [self.url_temp.format(i) for i in range(1,14)]

    def parse_url(self,url):
        print("----4----")
        response = requests.get(url,headers = self.headers)
        return response.content.decode()

    def get_content_list(self,html_str):
        print("----5----")
        html_element = etree.HTML(html_str)
        print(html_element)
        div_list = html_element.xpath("//div[@id='content-left']/div")
        print(div_list)
        content_list = []
        for div in div_list:
            item = {}
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            item["content"] = [i.replace("\n", "") for i in item["content"]]
            item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
            # print(item["author_gender"])
            item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "") if len(item["author_gender"]) > 0 else None
            item["auhtor_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
            item["auhtor_age"] = item["auhtor_age"][0] if len(item["auhtor_age"]) > 0 else None
            item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/@src")
            item["content_img"] = "https:" + item["content_img"][0] if len(item["content_img"]) > 0 else None
            item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
            item["author_img"] = "https:" + item["author_img"][0] if len(item["author_img"]) > 0 else None
            item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
            item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"]) > 0 else None
            # print(item)
            content_list.append(item)
        return content_list

    def save_content_list(self,content_list):
        print("----6----")
        for i in content_list:
            print(type(i))
            str = json.dumps(i,ensure_ascii=False)
            with open("qiushibaike.txt","a") as f:
                f.write(str)

    def run(self):
        print("----2----")
        # 获取url列表
        url_list = self.get_url_list()
        # 发送请求,获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # print(html_str)
            # 提取数据
            content_list = self.get_content_list(html_str)
            # print(content_list)
            # 保存
            self.save_content_list(content_list)

if __name__ == '__main__':
    print("----1----")
    qiubai = QiubaiSpider()
    qiubai.run()
