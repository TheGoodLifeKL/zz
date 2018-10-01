# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://dangdang.com/']
    redis_key = "dangdang"
    def parse(self, response):
        # 大分类列表
        div_list = response.xpath("//div[@class='con flq_body']/div")
        for div in div_list:
            item = {}
            item["b_cate"] = div.xpath("./dl/dt//text()").extract()
            item["b_cate"] = [i.strip() for i in item["b_cate"] if len(i.strip())>0]
            # 中间分类分组
            dl_list = div.xpath("./div//dl[@class='inner_dl']")
            for dl in dl_list:
                pass

