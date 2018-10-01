# -*- coding: utf-8 -*-
import urllib

import scrapy
from copy import deepcopy


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/mo/q---F5FC946C1C9D707337983F6DB88F87CE%3AFG%3D1--1-3-0----wapp_1532262751258_217/m?kw=%E8%99%8E%E7%89%99%E7%9B%B4%E6%92%AD&lp=5011&lm=&pn=0']

    def parse(self, response):
        div_list = response.xpath("//div[contains(@class,'i')]")
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./a/text()").extract_first()
            item["href"] = div.xpath("./a/@href").extract_first()
            item["img_list"] = []
            if item["href"] is not None:
                item["href"] = urllib.parse.urljoin(response.url,item["href"])
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_detail,
                    meta={"item":deepcopy(item)}
                )
    def parse_detail(self,response):
        item = response.meta["item"]
        # if "img_list" not in item:
        #     item["img_list"] = response.xpath("//a[text()='图']/@href").extract()
        # else:
        item["img_list"].extend(response.xpath("//a[text()='图']/@href").extract())
        # item["img_list"] =
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url is not None:
            next_url = urllib.parse.urljoin(response.url,next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_detail,
                meta={"item":item}
            )
        print(item)
