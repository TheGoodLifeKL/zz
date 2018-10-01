# -*- coding: utf-8 -*-
from pymongo import MongoClient

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

client = MongoClient()
collection = client["tencent"]["hr"]

class TencentPipeline(object):
    def process_item(self, item, spider):
        print(item)
        # print(type(item))
        collection.insert(dict(item))
        return item
