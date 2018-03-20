# -*- coding: utf-8 -*-
# 注意json文件以一个空的字典{}结尾！
import json
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#此管道处理函数 用于处理 distinct_spider.py 中 的爬虫数据
class href_JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('href.json', 'w', encoding='utf-8')
        self.file.write('[')
        #print "Open the spider pipeline"

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

    #要特别注意这两个函数名，因为框架需要调用 因此名字必须是open_spider 一点都不能错
    def open_spider(self,spider):
        pass
        #print "Spider start!"

    #同样 close_spider 的函数名也必须是这个，否则框架是无法识别的
    def close_spider(self, spider):
        #print "Close the spider pipeline"
        #注意Json文件以一个空的数据结构结尾
        self.file.write('{}]')
        self.file.close()

#此管道处理函数 用于处理 house_spider.py 中 的爬虫数据
class houseInfo_JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('houseInfo.json', 'w', encoding='utf-8')
        self.file.write('[')
        #print "Open the spider pipeline"

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

    #要特别注意这两个函数名，因为框架需要调用 因此名字必须是open_spider 一点都不能错
    def open_spider(self,spider):
        pass
        #print "Spider start!"

    #同样 close_spider 的函数名也必须是这个，否则框架是无法识别的
    def close_spider(self, spider):
        #print "Close the spider pipeline"
        #注意Json文件以一个空的数据结构结尾
        self.file.write('{}]')
        self.file.close()

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item
