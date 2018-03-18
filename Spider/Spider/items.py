# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#这个类适用于存储城区名和其url的数据结构 在spider中注意区分!
class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_distinct = scrapy.Field()
    href_distinct = scrapy.Field()
    pass

#这个类用于存储各社区(街道)的名字和url 在spider中注意区分!
class CommunityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_community = scrapy.Field()
    href_community = scrapy.Field()
    pass
