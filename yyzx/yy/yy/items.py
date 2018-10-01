# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_title = scrapy.Field()
    article_href = scrapy.Field()
    periods = scrapy.Field()
    detail = scrapy.Field()
    pre_href = scrapy.Field()

