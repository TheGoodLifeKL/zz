# coding:utf-8
import requests
from lxml import etree
import json


class TiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "https://tieba.baidu.com/mo/q---F5FC946C1C9D707337983F6DB88F87CE%3AFG%3D1--1-1-0--2--wapp_1531904372574_685/m?kw="+tieba_name+"&pn=0"
        self.part_url = "https://tieba.baidu.com/mo/q---F5FC946C1C9D707337983F6DB88F87CE%3AFG%3D1--1-1-0--2--wapp_1531904372574_685/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        }

    def parse_url(self,url):
        print(url)
        response = requests.get(url,headers = self.headers)
        # print(response.content)
        return response.content

    def get_content_list(self,html_str): # 提取数据
        html = etree.HTML(html_str)
        detail_div_list = html.xpath("//div[@class='i'] | div[@class='i x']")
        # print(detail_div_list)
        content_list = []
        for div in detail_div_list:
            item = {}
            item["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()"))>0 else None
            item["href"] = self.part_url + div.xpath("./a/@href")[0] if len(div.xpath("./a/@href"))>0 else None
            item["img_list"] = self.get_image_list(item["href"],[])
            content_list.append(item)
        # 提取下一页的url地址
        next_url = self.part_url + html.xpath("//a[text()='下一页']/@href")[0] if len(html.xpath("//a[text()='下一页']/@href"))>0 else None
        return content_list,next_url

    def get_image_list(self,detail_url,total_image_list):
        detail_html_str = self.parse_url(detail_url)
        print("*"*100)
        print(detail_html_str.decode())
        print("*"*100)
        detail_html = etree.HTML(detail_html_str)
        img_list = detail_html.xpath("//a[text()='图']/@href")
        print(img_list)
        total_image_list.extend(img_list)
        detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")
        if len(detail_next_url)>0:
            detail_next_url = self.part_url + detail_next_url[0]
            return self.get_image_list(detail_next_url,total_image_list)
        return total_image_list


    def save_content_list(self,content_list):
        file_path = self.tieba_name + ".txt"
        with open(file_path,"a") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write("\n")
            print("保存成功")


    def run(self):
        next_url = self.start_url
        while next_url is not None:
            # start_url
            # 发送请求,获取响应
            html_str = self.parse_url(next_url)
            # 提取数据,获取下一页的url地址
            content_list,next_url = self.get_content_list(html_str)
            print(content_list)

                # 提取列表页的url和title
                # 请求列表页的url,获取详情页的第一页
                #　提取详情页第一页的图片,获取下一页的url
                # 请求详情页的url,进入循环
            # 保存数据
            self.save_content_list(content_list)
            #　请求下一页的url地址,循环


if __name__ == '__main__':
    tieba_spider = TiebaSpider("lol")
    tieba_spider.run()