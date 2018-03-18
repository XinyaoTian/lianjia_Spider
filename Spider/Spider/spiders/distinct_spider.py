# -*- encoding:utf-8 -*-
import scrapy

from Spider.items import SpiderItem

from scrapy.contrib.spiders import CrawlSpider, Rule

class HrefSpider(CrawlSpider):

    name = "hrefspider"

    allowed_domains = ["lianjia.com"]

    start_urls = [
        "https://bj.lianjia.com/ershoufang/"
    ]

    def parse(self,response):
        print "********************New page*********************"
        for info in response.xpath('//*[@id="position"]/dl[2]/dd/div[1]/div/a'):
            infoItem = SpiderItem()
            infoItem["name_distinct"] = info.xpath('.//text()').extract_first()
            print infoItem["name_distinct"]
            yield infoItem
