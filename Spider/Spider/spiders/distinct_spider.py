# -*- encoding:utf-8 -*-
import scrapy

import logging
logging.basicConfig(level = logging.INFO)

from Spider.items import SpiderItem
from Spider.items import CommunityItem

from scrapy.contrib.spiders import CrawlSpider, Rule

class HrefSpider(CrawlSpider):

    name = "hrefspider"

    #使用管道端口 300
    custom_settings = {
        'ITEM_PIPELINES':{
            'Spider.pipelines.href_JsonWithEncodingPipeline':300
        }
    }

    allowed_domains = ["lianjia.com"]

    start_urls = [
        "https://bj.lianjia.com/ershoufang/"
    ]

    def parse_community(self,response):
        logging.info("********************New page*********************")
        for info in response.xpath('//*[@id="position"]/dl[2]/dd/div[1]/div[2]/a'):
            infoItem = CommunityItem()
            infoItem["name_community"] = info.xpath('.//text()').extract_first()
            distinct_link = info.xpath('.//@href').extract_first()
            infoItem["href_community"] = response.urljoin(distinct_link)
            logging.info(infoItem["name_community"])
            logging.info(infoItem["name_community"])
            yield infoItem


    def parse(self,response):
        logging.info("********************New page*********************")
        for info in response.xpath('//*[@id="position"]/dl[2]/dd/div[1]/div/a'):
            infoItem = SpiderItem()
            infoItem["name_distinct"] = info.xpath('.//text()').extract_first()
            distinct_link = info.xpath('.//@href').extract_first()
            infoItem["href_distinct"] = response.urljoin(distinct_link)
            logging.info(infoItem["name_distinct"])
            logging.info(infoItem["href_distinct"])
            next_page = infoItem["href_distinct"]
            if next_page is not None:
                #print next_page

                #注意这里一定要写 yield 才可以继续发起请求
                yield scrapy.Request(next_page,callback=self.parse_community)



            #print response.urljoin(infoItem["href_distinct"])
