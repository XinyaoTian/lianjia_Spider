# -*- encoding:utf-8 -*-
import scrapy

import logging
logging.basicConfig(level = logging.INFO)

from Spider.items import HouseItem

from scrapy.contrib.spiders import CrawlSpider, Rule

class HouseSpider(CrawlSpider):

    name = "housespider"

    allowed_domains = ["lianjia.com"]

    start_urls = [
        "https://bj.lianjia.com/ershoufang/taipingqiao1/"
    ]

    def parse(self,response):
        logging.info("********************New page*********************")
        for info in response.xpath('//div[@class="info clear"]'):
            infoItem = HouseItem()
            infoItem["introduction_house"] = info.xpath('.//div[1]/a/text()').extract_first()


            logging.info(infoItem["introduction_house"])

        # #print response
        # page_info = response.xpath('//div[@class="page-box fr"]/div[1]/@page-data').extract_first()
        # print type(page_info)
        # page_info = str(page_info)
        # print type(page_info)
        # #page_info = dict(page_info)
        # #full_page = page_info["totalPage"]
        # #current_page = page_info["curPage"]
        # print page_info
        # #print full_page
        # #print current_page




