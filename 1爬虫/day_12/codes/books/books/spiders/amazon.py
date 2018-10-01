# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls = ['http://amazon.cn/']
    redis_key = "amazon"

    rules = (
        # 匹配大分类的url
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='a-unordered-list a-nostyle a-vertical s-ref-indent-one']//li")),callback="parse_b_cate", follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='left_nav browseBox']/ul[2]/li")),follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li//h2/..")),callback="parse_book_detail")
    )

    def parse_b_cate(self, response):
        item = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item["b_cate_name"] = response.xpath('.//ul[@class="a-unordered-list a-nostyle a-vertical s-ref-indent-one"]//li//span/a/text()').extract_first()
        print(item)
        yield scrapy.Request(
            
        )
    def parse_book_detail(self, response):
        item = {}
        item["book_title"] = response.xpath("//span[@id='productTitle']/text()").extract_first()
        print(item)