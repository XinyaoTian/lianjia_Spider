# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#这个类适用于处理并暂存城区名和其url的数据结构 在spider中注意区分!
#Be used in distinct_spider.py
class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_distinct = scrapy.Field()
    href_distinct = scrapy.Field()
    pass

#这个类用于处理并暂存各社区(街道)的名字和url 在spider中注意区分!
#Be used in distinct_spider.py
class CommunityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_community = scrapy.Field()
    href_community = scrapy.Field()
    pass

#这个类用于处理并暂存房屋的具体信息
#Be used in house_spider.py
class HouseItem(scrapy.Item):
    introduction_house = scrapy.Field() #房子介绍
    href_house = scrapy.Field() #房子具体信息的url
    community_house = scrapy.Field() #所在小区
    unit_house = scrapy.Field() #户型
    size_house = scrapy.Field() #房屋面积
    direction_house = scrapy.Field() #朝向
    decoration_house = scrapy.Field() #装修程度:简装 精装 等等
    elevator_house = scrapy.Field() #有无电梯
    type_house = scrapy.Field() #楼型: 高层 板房 等等
    years_house = scrapy.Field() #房屋建成时间
    area_house = scrapy.Field() #房屋所在区域(与片区关键字检索有关)
    interests_house = scrapy.Field() #收藏数
    watch_times = scrapy.Field() #带看次数
    submit_period = scrapy.Field() #多久以前发布
    years_period = scrapy.Field() #产权:满两年
    tax_free = scrapy.Field() #满五年 即 无需交税
    total_price = scrapy.Field() #房屋总价
    smeter_price = scrapy.Field() #每平米单价
    pass
