# -*- coding: utf-8 -*-

import scrapy
from copy import deepcopy
import json
import urllib


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com','p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl/dt")
        for dt in dt_list:
            item = {}
            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            em_list = dt.xpath("./following-sibling::dd/em")
            for em in em_list:
                item["s_name"] = em.xpath("./a/text()").extract_first()
                item["s_href"] = em.xpath("./a/@href").extract_first()
                # print(item)
                if item["s_href"] is not None:
                    item["s_href"] = "https:" + item["s_href"]
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.parse_book_list,
                        meta={"item":deepcopy(item)}
                    )

    def parse_book_list(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@id='plist']//li")
        for li in li_list:
            item["book_img"] = li.xpath(".//a/img/@src").extract_first()
            if item["book_img"] is None:
                item["book_img"] = li.xpath(".//a/img/@data-lazy-img").extract_first()
            item["book_img"] = "https:" + item["book_img"] if item["book_img"] is not None else None
            item["book_name"] = li.xpath(".//div[@class='p-name']/a/em/text()").extract_first()
            item["book_author"] = li.xpath(".//span[@class='author_type_1']/a/text()").extract_first()
            item["book_process"] = li.xpath(".//span[@class='p-bi-store']/a/text()").extract_first()
            item["publish_date"] = li.xpath(".//span[@class='p-bi-date']/text()").extract_first()
            item["book_sku"] = li.xpath("./div/@data-sku").extract_first()
            print(item["book_sku"])
            yield scrapy.Request(
                "https://p.3.cn/prices/mgets?skuIds=J_{}".format(item["book_sku"]),
                callback=self.parse_price,
                meta={"item":deepcopy(item)}
            )
            # print("+"*100)

        next_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            next_url = urllib.parse.urljoin(response.url,next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                meta={"item":item}
            )
            # print("-"*100)

    def parse_price(self,response):
        print("*"*100)
        item = response.meta["item"]
        print(json.loads(response.body.decode()))
        print("*"*100)
        item["book_price"] = json.loads(response.body.decode())[0]["op"]
        print(item)







