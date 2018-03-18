# -*- coding: utf-8 -*-
import json
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('href.json', 'w', encoding='utf-8')
        #self.file.write('[')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        #self.file.write(']')
        self.file.close()

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item
