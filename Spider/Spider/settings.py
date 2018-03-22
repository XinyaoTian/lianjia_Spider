# -*- coding: utf-8 -*-

#引入我们编写的功能类中的功能函数
from func_pack import create_daytime_table
from func_pack import create_time_table

# Scrapy settings for Spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Spider'

SPIDER_MODULES = ['Spider.spiders']
NEWSPIDER_MODULE = 'Spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#我将设置中的对数据处理的流水线内置在了spider文件中
#即spider文件中的 custom_settings 变量决定每个爬虫究竟使用哪个流水线
# ITEM_PIPELINES = {
#     "Spider.pipelines.JsonWithEncodingPipeline": 300,
# }

#-----2018-3-21------
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "Lianjia_houseInfo"  # 库名
MONGO_COLL = create_time_table()  # collection名
# MONGO_USER = "zhangsan"
# MONGO_PSW = "123456"
#-------------------

#-----2018-3-22------
COOKIE = {'ljref': 'pc_sem_baidu_ppzq_x', 'Qs_pv_200116': '3112381745763005000%2C3149859735597147600', 'all-lj': '39e8d71f7d4bc70e2283e0ca888864de', '_jzqa': '1.2811990290111634400.1502104083.1521592576.1521715567.18', '_jzqc': '1', '_jzqb': '1.2.10.1521715567.1', '_qzjto': '2.1.0', 'Hm_lpvt_9152f8221cb6243a53c83b956842be8a': '1521715570', 'select_city': '110000', '_smt_uid': '59884a12.252f6cd4', 'gr_user_id': '49e91f68-009d-4b8b-8d02-8c31c268cb6b', '_jzqy': '1.1521120393.1521715567.2.jzqsr', '_jzqx': '1.1521357932.1521540918.5.jzqsr', '_gid': 'GA1.2.2144421825.1521715572', '_ga': 'GA1.2.946537891.1502104084', 'CNZZDATA1254525948': '1604218046-1521114475-%7C1521713755', '_qzja': '1.1510458665.1502104082820.1521592576409.1521715567523.1521715567523.1521715570408.0.0.0.95.18', '_qzjc': '1', '_qzjb': '1.1521715567522.2.0.0.0', 'UM_distinctid': '16229ab27fe6be-000c12ce97d136-b353461-e1000-16229ab27ff95', '_jzqckmp': '1', 'CNZZDATA1255633284': '1458695289-1521112239-%7C1521713824', 'lianjia_ssid': 'dd7eb92e-f3a7-4ba6-8afe-16c9099af6d2', 'CNZZDATA1255604082': '1607816614-1521112886-%7C1521713827', 'CNZZDATA1253477573': '1723547860-1521113027-%7C1521710379', 'Qs_lvt_200116': '1521354831', 'lianjia_uuid': '7809f78e-b5c2-4047-9bbe-7150bafb1f3d', 'Hm_lvt_9152f8221cb6243a53c83b956842be8a': '1521117506,1521120392,1521438829,1521715567'}

#--------------------

# 设置等待时间
DOWNLOAD_DELAY = 0.4




# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Spider.middlewares.SpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Spider.pipelines.SpiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
