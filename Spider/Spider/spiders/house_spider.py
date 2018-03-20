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
        "https://bj.lianjia.com/ershoufang/miyunqita11/"
    ]

    #此函数用于处理房屋信息
    def parse_house_info(self,response):
        logging.info("********************New page*********************")
        for info in response.xpath('//div[@class="info clear"]'):
            infoItem = HouseItem()
            infoItem["introduction_house"] = info.xpath('.//div[@class="title"]/a/text()').extract_first()
            infoItem["href_house"] = info.xpath('.//div[@class="title"]/a/@href').extract_first()
            infoItem["community_house"] = info.xpath('.//div[@class="houseInfo"]/a[1]/text()').extract_first()
            infoItem["unit_house"] = info.xpath('.//div[@class="houseInfo"]/text()[1]').extract_first()
            infoItem["size_house"] = info.xpath('.//div[@class="houseInfo"]/text()[2]').extract_first()
            infoItem["direction_house"] = info.xpath('.//div[@class="houseInfo"]/text()[3]').extract_first()
            infoItem["decoration_house"] = info.xpath('.//div[@class="houseInfo"]/text()[4]').extract_first()
            infoItem["elevator_house"] = info.xpath('.//div[@class="houseInfo"]/text()[5]').extract_first()
            infoItem["type_house"] = info.xpath('.//div[@class="positionInfo"]/text()[1]').extract_first()
            infoItem["years_house"] = info.xpath('.//div[@class="positionInfo"]/text()[2]').extract_first()
            infoItem["area_house"] = info.xpath('.//div[@class="positionInfo"]/a[1]/text()').extract_first()
            infoItem["interests_house"] = info.xpath('.//div[@class="followInfo"]/text()[1]').extract_first()
            infoItem["watch_times"] = info.xpath('.//div[@class="followInfo"]/text()[2]').extract_first()
            infoItem["submit_period"] = info.xpath('.//div[@class="timeInfo"]/text()[1]').extract_first()
            infoItem["years_period"] = info.xpath('.//div[@class="tag"]/span[@class="five"]/text()').extract_first()
            infoItem["tax_free"] = info.xpath('.//div[@class="tag"]/span[@class="taxfree"]/text()').extract_first()


            logging.info(infoItem["introduction_house"])
            logging.info(infoItem["href_house"])
            logging.info(infoItem["community_house"])
            logging.info(infoItem["unit_house"])
            logging.info(infoItem["size_house"])
            logging.info(infoItem["direction_house"])
            logging.info(infoItem["decoration_house"])
            logging.info(infoItem["elevator_house"])
            logging.info(infoItem["type_house"])
            logging.info(infoItem["years_house"])
            logging.info(infoItem["area_house"])
            logging.info(infoItem["interests_house"])
            logging.info(infoItem["submit_period"])
            logging.info(infoItem["tax_free"])

    #此函数用于发起请求计算总页数并翻页
    def parse(self,response):
        #这里需要计算出该社区房子共有多少页，便于爬虫的翻页
        houses_per_page = len(response.xpath('//div[@class="info clear"]'))
        houses_total = int(response.xpath('//*[@id="leftContent"]/div[1]/h2/span/text()').extract_first())

        #计算总页数
        if houses_total%houses_per_page is not 0:
            full_page = houses_total // houses_per_page + 1
        else:
            full_page = houses_total // houses_per_page

        #设置当前页数，并通过循环 利用scrapy.Request函数依次对后续页数发起请求
        #并用自己编写的parse_house_info函数对新抓取到的页面进行信息搜集
        cur_page = 1
        while cur_page <= full_page:
            #手动组合字符串url
            part_url = "pg" + str(cur_page) +"/"
            cur_url = response.urljoin(part_url)
            yield scrapy.Request(cur_url,callback=self.parse_house_info)
            cur_page += 1



