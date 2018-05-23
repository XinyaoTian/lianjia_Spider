# -*- encoding:utf-8 -*-
import scrapy

import logging
logging.basicConfig(level = logging.INFO)

from Spider.items import HouseItem

from scrapy.contrib.spiders import CrawlSpider, Rule

from scrapy.conf import settings

from func_pack import get_current_day
from func_pack import get_current_time

#这个方法 用于获取所有的社区初始URL。
#丢给start_urls可以实现全部北京房子的爬虫
#前提是必须运行distinct_spider 保证href.json中已经存在相关数据

from func_pack import get_comhrefs

class HouseSpider(CrawlSpider):

    name = "housespider"

    #使用管道端口 301
    custom_settings = {
        'ITEM_PIPELINES':{
            # 'Spider.pipelines.MongoDB_StoragePipeline':301,
            'Spider.pipelines.houseInfo_JsonWithEncodingPipeline':301
        }
    }

    headers = {
        "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8",
        "Accept - Encoding":"gzip, deflate",
        "Accept - Language":"zh - CN, zh;q = 0.9",
        "Cache - Control":"max - age = 0",
        "Connection":"keep - alive",
        "Host": "bj.lianjia.com",
        "Referer":" http: // bj.lianjia.com /?utm_source = baidu & utm_medium = pinzhuan & utm_term = biaoti & utm_content = biaotimiaoshu & utm_campaign = sousuo & ljref = pc_sem_baidu_ppzq_x",
        "Upgrade - Insecure - Requests":"1",
        "User - Agent":"Mozilla / 5.0(WindowsNT10.0;Win64; x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 64.0.3282.186 Safari / 537.36"
    }

    meta = {
        'dont_redirect':True,
        'handle_httpstatus_list': [301, 302]
    }

    cookie = settings['COOKIE']

    allowed_domains = ["lianjia.com"]

    # 测试用的start_urls 运行时把它注释掉
    # start_urls = [
    #     "https://bj.lianjia.com/ershoufang/miyun/"
    # ]

    #将提取好的房源片区首页丢给 start_urls 项目就可以开始跑了
    start_urls = get_comhrefs()

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
            infoItem["years_period"] = info.xpath('.//div[@class="followInfo"]/div[@class="tag"]/span[@class="five"]/text()').extract_first()
            infoItem["tax_free"] = info.xpath('.//div[@class="followInfo"]/div[@class="tag"]/span[@class="taxfree"]/text()').extract_first()
            infoItem["total_price"] = info.xpath('.//div[@class="totalPrice"]/span[1]/text()').extract_first()
            infoItem["smeter_price"] = info.xpath('.//div[@class="unitPrice"]/span[1]/text()').extract_first()
            infoItem["scrape_time"] = get_current_day()+"_"+get_current_time()


            logging.info(infoItem["introduction_house"])
            logging.info(infoItem["href_house"])
            # logging.info(infoItem["community_house"])
            # logging.info(infoItem["unit_house"])
            # logging.info(infoItem["size_house"])
            # logging.info(infoItem["direction_house"])
            # logging.info(infoItem["decoration_house"])
            # logging.info(infoItem["elevator_house"])
            # logging.info(infoItem["type_house"])
            # logging.info(infoItem["years_house"])
            # logging.info(infoItem["area_house"])
            # logging.info(infoItem["interests_house"])
            # logging.info(infoItem["watch_times"])
            # logging.info(infoItem["submit_period"])
            # logging.info(infoItem["years_period"])
            # logging.info(infoItem["tax_free"])

            yield infoItem


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
            print response.meta
            yield scrapy.Request(cur_url,callback=self.parse_house_info)
            cur_page += 1



