# -*- encoding:utf-8 -*-
import scrapy

from Spider.items import SpiderItem

from scrapy.contrib.spiders import CrawlSpider, Rule

class HrefSpider(CrawlSpider):

    name = "hrefspider"