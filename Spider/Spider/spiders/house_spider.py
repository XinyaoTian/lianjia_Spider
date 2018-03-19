# -*- encoding:utf-8 -*-
import scrapy

import logging
logging.basicConfig(level = logging.INFO)

from Spider.items import HouseItem

from scrapy.contrib.spiders import CrawlSpider, Rule

class HouseSpider(CrawlSpider):

    name = "housespider"

    allowed_domains = ["lianjia.com"]

    start_urls = []

