# -*- encoding:utf-8 -*-
import scrapy

import logging
logging.basicConfig(level = logging.DEBUG)

from Spider.items import HouseItem

from scrapy.contrib.spiders import CrawlSpider, Rule

from scrapy.conf import settings

from func_pack import get_current_day
from func_pack import get_current_time

import re

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
            # 'Spider.pipelines.houseInfo_JsonWithEncodingPipeline':301
            'Spider.pipelines.houseInfo_CsvWithEncodingPipeline': 301
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
    #     "https://bj.lianjia.com/ershoufang/miyun/",
    #     "https://xm.lianjia.com/ershoufang/douxilu/",
    #     "https://zz.lianjia.com/ershoufang/jinshui/",
    #     "https://sh.lianjia.com/ershoufang/beicai/"
    # ]

    # 房源为0的网页
    # start_urls = [
    #     "https://sh.lianjia.com/ershoufang/nantong/"
    # ]

    # 将提取好的房源片区首页丢给 start_urls 项目就可以开始跑了
    start_urls = get_comhrefs()

    def parse_notbj_house_info(self,response):
        for info in response.xpath('//div[@class="info clear"]'):
            infoItem = HouseItem()
            infoItem["introduction_house"] = info.xpath('.//div[@class="title"]/a/text()').extract_first()
            infoItem["href_house"] = info.xpath('.//div[@class="title"]/a/@href').extract_first()
            infoItem["community_house"] = info.xpath('.//div[@class="houseInfo"]/a[1]/text()').extract_first()
            # 由于其他地区的链家二手房界面的消息是一大条，所以需要借用正则切除
            infoItem["info_cluster"] = info.xpath('.//div[@class="houseInfo"]/text()').extract_first()
            # info_list = re.split(r'\|',info.xpath('.//div[@class="houseInfo"]/text()').extract_first() )
            # infoItem["unit_house"] = info_list[1]
            infoItem["unit_house"] = None
            # infoItem["size_house"] = info_list[2]
            infoItem["size_house"] = None
            # infoItem["direction_house"] = info_list[3]
            infoItem["direction_house"] = None
            # infoItem["decoration_house"] = info_list[4]
            infoItem["decoration_house"] = None
            infoItem["elevator_house"] = None
            # 同样需要切割
            infoItem["info_flood"] = info.xpath('.//div[@class="positionInfo"]/text()').extract_first()
            # infoItem["type_house"] = re.split(r'\d{4}',info.xpath('.//div[@class="positionInfo"]/text()').extract_first())[0]
            infoItem["type_house"] = None
            # infoItem["years_house"] = re.split(r'\)',info.xpath('.//div[@class="positionInfo"]/text()').extract_first())[1]
            infoItem["years_house"] = None
            infoItem["area_house"] = info.xpath('.//div[@class="positionInfo"]/a[1]/text()').extract_first()

            # 这里同样需要切割
            infoItem['info_follow'] = info.xpath('.//div[@class="followInfo"]/text()').extract_first()
            # info_list = re.split(r'\/', info.xpath('.//div[@class="followInfo"]/text()').extract_first())
            # infoItem["interests_house"] = info_list[0]
            infoItem["interests_house"] = None
            # infoItem["watch_times"] = info_list[1]
            infoItem["watch_times"] = None
            # infoItem["submit_period"] = info_list[2]
            infoItem["submit_period"] = None

            infoItem["years_period"] = info.xpath('.//div[@class="followInfo"]/div[@class="tag"]/span[@class="five"]/text()').extract_first()
            infoItem["tax_free"] = info.xpath('.//div[@class="followInfo"]/div[@class="tag"]/span[@class="taxfree"]/text()').extract_first()
            infoItem["total_price"] = info.xpath('.//div[@class="totalPrice"]/span[1]/text()').extract_first()
            infoItem["smeter_price"] = info.xpath('.//div[@class="unitPrice"]/span[1]/text()').extract_first()

            infoItem["region"] = re.split(r'//', re.split(r'.lianjia.com.', str(infoItem["href_house"]))[0])[1]

            yield infoItem


    #此函数用于处理"北京"房屋信息
    def parse_house_info(self,response):
        # logging.info("********************New page*********************")
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
            # infoItem["scrape_time"] = get_current_day()+"_"+get_current_time()
            # 把url中的地区抽出来单独变成一个字段，方便后续的 数据预处理 和 数据分析
            infoItem["region"] = re.split(r'//',re.split(r'.lianjia.com.',str(infoItem["href_house"]))[0])[1]
            infoItem["info_cluster"] = None
            infoItem["info_flood"] = None
            infoItem["info_follow"] = None
            yield infoItem


    #此函数用于发起请求计算总页数并翻页
    def parse(self,response):
        #这里需要计算出该社区房子共有多少页，便于爬虫的翻页
        houses_per_page = len(response.xpath('//div[@class="info clear"]'))
        houses_total = int(response.xpath('//div[@class="leftContent"]/div[@class="resultDes clear"]/h2/span/text()').extract_first())
        # houses_total = int(
        #     response.xpath('/html/body/div[4]/div[1]/div[@class="resultDes clear"]/h2/span/text()').extract_first())

        #计算总页数
        if houses_per_page == 0:
            pass
        else:
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
                # print response.meta
                if re.split(r'//',re.split(r'.lianjia.com.',str(cur_url))[0])[1] == "bj":
                    yield scrapy.Request(cur_url,callback=self.parse_house_info)
                else:
                    yield scrapy.Request(cur_url, callback=self.parse_notbj_house_info)
                cur_page += 1



