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
        # 真是为难记不清行政区划分的理科生了...
        "https://bj.lianjia.com/ershoufang/",# 北京——北京市
        # "https://sh.lianjia.com/ershoufang/",# 上海——上海市
        # "https://gz.lianjia.com/ershoufang/",# 广州——广州省
        # "https://sz.lianjia.com/ershoufang/",# 深圳——深圳市
        # "https://tj.lianjia.com/ershoufang/",# 天津
        # "https://hz.lianjia.com/ershoufang/",# 杭州
        # "https://zz.lianjia.com/ershoufang/",# 郑州
        # "https://nj.lianjia.com/ershoufang/",# 南京
        # "https://wh.lianjia.com/ershoufang/",# 武汉
        # "https://dl.lianjia.com/ershoufang/",# 大连
        # "https://xm.lianjia.com/ershoufang/",# 厦门
        # "https://qd.lianjia.com/ershoufang/",# 青岛
        # "https://cd.lianjia.com/ershoufang/",# 成都
        # "https://cq.lianjia.com/ershoufang/",# 重庆——重庆市
        # "https://cs.lianjia.com/ershoufang/",# 长沙
        # "https://su.lianjia.com/ershoufang/",# 苏州
        # "https://sjz.lianjia.com/ershoufang/",# 石家庄
        # "https://hf.lianjia.com/ershoufang/"# 合肥——安徽省
    ]
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)

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
