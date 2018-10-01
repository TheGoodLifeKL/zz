# coding:utf-8
from selenium import webdriver
import json
import time

class HuyaSpider:
    def __init__(self):
        # self.start_url = "https://www.douyu.com/directory/game/yz"
        self.start_url = "https://www.huya.com/g/xingxiu"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        # li_list = self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")
        li_list = self.driver.find_elements_by_xpath("//ul[@class='live-list clearfix']/li")
        content_list = []
        for li in li_list:
            item = {}
            item["anchor_name"] = li.find_element_by_xpath(".//i[@class='nick']").text
            # item["room_image"] = li.find_element_by_xpath(".//span[@class='imgbox']/img").get_attribute("src")
            # item["room_title"] = li.find_element_by_xpath(".//div[@class='mes-tit']//h3[@class='ellipsis']").text
            # item["watcher_num"] = li.find_element_by_xpath(".//span[@class='dy-num fr']").text
            # item["anchor_name"] = li.find_element_by_xpath(".//span[@class='dy-name ellipsis fl']").text
            # item["room_cate"] = li.find_element_by_xpath(".//span[@class='tag ellipsis']").text
            print(item)
            content_list.append(item)
        # 获取下一页的url
        # next_url = self.driver.find_elements_by_xpath("//a[@class='shark-pager-next']")
        next_url = self.driver.find_elements_by_xpath("//a[@class='laypage_next']")
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list,next_url

    def save_data(self,content_list):
        with open("huya.txt","a") as f:
            for content in content_list:
                content = json.dumps(content,ensure_ascii=False)
                f.write(content)
                f.write("\n\n")

    def run(self):
        # 获取start_url
        # 发送请求,获取响应
        self.driver.get(self.start_url)
        # 提取数据,获取下一页url
        content_list,next_url = self.get_content_list()
        # 保存数据
        self.save_data(content_list)
        # 点击下一页(循环)
        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list,next_url = self.get_content_list()
            self.save_data(content_list)

if __name__ == '__main__':
    douyu = HuyaSpider()
    douyu.run()