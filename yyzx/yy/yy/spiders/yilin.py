# -*- coding: utf-8 -*-
import urllib

import scrapy
from copy import deepcopy
import re


class YilinSpider(scrapy.Spider):
    name = 'yilin'
    allowed_domains = ['92yilin.com']
    start_urls = ['http://www.92yilin.com']

    def parse(self, response):
        td_list = response.xpath("//div[@id='tagContent0']/table//td[@class='time']")
        for td in td_list:
            item = {}
            item["periods"] = td.xpath("./a/text()").extract_first()
            item["pre_href"] = td.xpath("./a/@href").extract_first()
            if item["pre_href"] is not None:
                item["pre_href"] = "http://www.92yilin.com/" + item["pre_href"]
            yield scrapy.Request(
                item["pre_href"],
                callback=self.parse_book_list,
                meta={"item":item}
            )

    def parse_book_list(self,response):
        # print("*"*100)
        item = response.meta["item"]
        span_list = response.xpath("//span[@class='maglisttitle']")
        for span in span_list:
            item["article_title"] = span.xpath("./a/@title").extract_first()
            item["article_href"] = span.xpath("./a/@href").extract_first()
            if item["article_href"] is not None:
                # item["article_href"] = "http://www.92yilin.com/" + item["article_href"]
                item["article_href"] = urllib.parse.urljoin(response.url,item["article_href"])
            yield scrapy.Request(
                item["article_href"],
                callback=self.parse_detail,
                meta={"item":item}
            )

    def parse_detail(self,response):
        item = response.meta["item"]
        item["detail"] = response.xpath("//div[@class='blkContainerSblkCon']/p/text()").extract()
        for i in item["detail"]:
            i.replace("\u3000\u3000","")
        print(item["detail"])
        yield item
        # print(item)


