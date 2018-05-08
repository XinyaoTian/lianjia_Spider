# -*- coding: utf-8 -*-

#引入我们编写的功能类中的功能函数
from func_pack import create_daytime_table
from func_pack import create_time_table
from func_pack import get_zhima_agency

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

'''连接MongoDB数据库的设置'''
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

# -----2018-3-27----- #
# USER_AGENTS 随机的代理头部
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# 手动添加代理设置
# 可以从芝麻ip上买稳定的IP。这里的IP都已经过期了。
# PROXIES = [
#     {'ip_port': '175.168.3.35:54675', 'user_pass': '','ip_status':1}
# ]

# 存放失效ip。若3次TCP协议连接均失败，则将 PROXIES 中的 ip 移入 UNAVAILABLE_PROXIES
UNAVAILABLE_PROXIES = []

PROXIES = []

# 自动添加代理
# 手动在芝麻购买 IP 后，将生成的http协议的json格式API连接放到这里即可。
# api_url = "http://webapi.http.zhimacangku.com/getip?num=20&type=2&pro=0&city=0&yys=0&port=1&pack=15902&ts=0&ys=0&cs=1&lb=1&sb=0&pb=45&mr=1&regions="
# PROXIES = get_zhima_agency(api_url)

# 设置等待时间
DOWNLOAD_DELAY = 1.6

'''需要使用ip池时，更新IP池并打开这些设置'''
COOKIES_ENABLED = False
# 设置DownLoader_middleware
# 插拔中间件需要仔细看文档，了解相应中间件的端口号。
# 把想要拔下来的中间件的值设为 None ； 插上去的自己写的组件，设为相应的流程参数。
# 可以自己去scrapy的包里找源码，在middlewares中粘贴源码并改写，然后插拔组件。示例——RetryMiddleware
DOWNLOADER_MIDDLEWARES = {
#    'myproject.middlewares.MyCustomDownloaderMiddleware': 543,
    'Spider.middlewares.RandomUserAgent': 1,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    #'Spider.middlewares.ProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware':None,
    'Spider.middlewares.RetryMiddleware':550
}

'''到此为止'''

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
