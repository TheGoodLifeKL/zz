# coding:utf-8
import requests
from lxml import etree
import json
import threading
from queue import Queue

class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
        }
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        print("----3----")
        # return [self.url_temp.format(i) for i in range(1,14)]
        for i in range(1,14):
            self.url_queue.put(self.url_temp.format(i))


    def parse_url(self):
        while True:
            print("----4----")
            url = self.url_queue.get()
            print(url)
            response = requests.get(url,headers = self.headers)
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
            print("----5----")
            html = etree.HTML(html_str)
            print(html)
            div_list = html.xpath("//div[@id='content-left']/div")
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
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            print("----6----")
            for i in content_list:
                print(type(i))
                str = json.dumps(i,ensure_ascii=False)
                with open("qiushibaike.txt","a") as f:
                    f.write(str)
            self.content_queue.task_done()

    def run(self):
        thread_list = []
        print("----2----")
        # 获取url列表
        for i in range(20):
            t_url = threading.Thread(target=self.get_url_list)
            thread_list.append(t_url)
        # 发送请求,获取响应
        for i in range(2):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
            # print(html_str)
            # 提取数据
        t_html = threading.Thread(target=self.get_content_list)
        thread_list.append(t_html)
            # print(content_list)
            # 保存
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True) # 把子线程设置位守护线程
            t.start()
        print("主线程结束")

        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join() # 让主线程等待阻塞,等待队列完成再完成

if __name__ == '__main__':
    print("----1----")
    qiubai = QiubaiSpider()
    qiubai.run()
