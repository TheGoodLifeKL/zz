# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab5240/module14430/page1.htm']

    # 定义提取url地址的规则
    rules = (
        Rule(LinkExtractor(allow=r"/web/site0/tab5240/info\d+\.htm"), callback='parse_item'),
        Rule(LinkExtractor(allow=r"/web/site0/tab5240/module14430/page\d+.htm"),follow=True),
    )

    def parse_item(self, response):
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        td_list = response.xpath("//table[@id='ess_ctr14430_ListC_Info_LstC_Info']//tr//td[@class='hui14']")
        item = {}
        item["title"] = re.findall("<!--TitleStart-->(.*?)<!--TitleEnd-->",response.body.decode())[0]
        item["publish_date"] = re.findall("发布时间：20\d{2}-\d{2}-\d{2}",response.body.decode())[0]
        print(item)
