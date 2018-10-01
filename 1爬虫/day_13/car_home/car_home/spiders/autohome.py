# -*- coding: utf-8 -*-
import scrapy
import json
import re

class AutohomeSpider(scrapy.Spider):
    name = 'autohome'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/javascript/NewSpecCompare.js']


    def parse(self, response):
        json_str = re.findall(r"\[.*\]",response.body.decode("gb2312"))[0]
        data = json.loads(json_str)
        for l1 in data:
            item = {}
            item["b_cate"] = l1["N"]
            for l2 in l1["List"]:
                item["m_cate"] = l2["N"]
                for l3 in l2["List"]:
                    item["s_cate"] = l3["N"]
                    item["href"] = "https://car.autohome.com.cn/price/series-{}.html".format(l3["I"])
                    yield scrapy.Request(
                        item["href"],
                        callback=self.parse_detail,
                        meta={"item":item}
                    )
                    # print("*"*100)
    def parse_detail(self,response):
        item = response.meta["item"]
        item["name"] = response.xpath('//div[@class="main-title"]/a/text()').extract_first()
        item["series"] = []
        div_list = response.xpath('//div[@id="divSeries"]/div')
        for div in div_list:
            peizhi = div.xpath('.//span[1]/text()').extract_first()
            li_list = div.xpath('.//ul/li')
            for li in li_list:
                serie = {}
                serie["peizhi"] = peizhi
                serie["name"] = li.xpath('.//a/text()').extract_first()
                serie["follow"] = li.xpath('.//div[@class="attention"]/span/@style').re_first(r"\d+")
                item["series"].append(serie)
                print(item)
        yield item










