# -*- coding:utf-8 -*-
import json
import time
import requests

#用于获取已经取得的全部社区的url地址
def get_comhrefs():
    with open("href.json",'r')as f:
        temp = json.loads(f.read())
        #注意json文件以一个空的字典{}结尾！
    f.close()
    list_href = []
    for item in temp:
        if bool(item) is True: #由于json文件中最后一个数据为空，因此设置此判断防止误读
            list_href.append(item["href_community"].encode('utf-8')) #注意这里unicode转为utf-8的方法...
    #print list_href
    return list_href

#获取当前系统日期
def get_current_day():
    current_day = str(time.strftime("%Y_%m_%d"))
    #print current_day
    return current_day

#获取当前系统时间
def get_current_time():
    current_time = str(time.strftime("%H_%M_%S"))
    return current_time

#创建新的数据库名字
#我们设计的爬虫是要部署到云服务器上 利用脚本在每天固定时间对链家网进行爬取的
#因此 我们把每天得到的数据存进不同的表中 方便以后做数据的趋势分析
def create_daytime_table():
    houseInfo = "houseInfo"
    table_name = houseInfo + "_" + get_current_day()
    return table_name

def create_time_table():
    houseInfo = "houseInfo"
    table_name = houseInfo + "_" + get_current_day() + "_" + get_current_time()
    return table_name

# 本函数使用芝麻代理的API接口(HTTP类型,json格式)
# 并将获取到的数据储存为以dict为单元的list，直接对接到 settings.py 的 PROXIES 中使用
def get_zhima_agency(url):
    ip_list = []
    # 尝试获取芝麻代理API接口的ip数据，并组成一个dict，之后放在list中
    try:
        result = requests.get(url)
        content_dict = json.loads(result.content)
        # 可以通过打印 content_dict 来确定从API接口获取到的ip数据结构
        for item in content_dict['data']:
            ip_port_dict = {}
            ip_port_str = str(item['ip']) + ":" + str(item['port'])
            ip_port_dict['ip_port'] = ip_port_str
            ip_port_dict['user_pass'] = ''
            ip_port_dict['ip_status'] = 1 # 初始化ip状态为1 即可用状态。随后如果TCP连续3次未连接上则置0。ip失效。
            ip_list.append(ip_port_dict)
    except:
        print "Warnning!Check your web connection or your ZhiMa Ip agency url status."
    finally:
        # 最终，打印并返回从API中获取的list
        print ip_list
        return ip_list

#这个函数是用于转化浏览器上开发者工具里复制粘贴下来的COOKIE的
#先把cookie那一栏粘贴上从浏览器复制下来的一大长串COOKIE
#运行这个文件，会打印出字典格式的COOKIE
#把这个字典格式的COOKIE复制粘贴到settings里面，再在相关爬虫文件里引用就可以啦
class transCookie():
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

# if __name__ == "__main__":
#     #这个是现在我的COOKIE 大家要根据自己的浏览器复制进自己的COOKIE哟
#     cookie = "lianjia_uuid=7809f78e-b5c2-4047-9bbe-7150bafb1f3d; _smt_uid=59884a12.252f6cd4; _ga=GA1.2.946537891.1502104084; UM_distinctid=16229ab27fe6be-000c12ce97d136-b353461-e1000-16229ab27ff95; Qs_lvt_200116=1521354831; Qs_pv_200116=3112381745763005000%2C3149859735597147600; _jzqx=1.1521357932.1521540918.5.jzqsr=bj%2Elianjia%2Ecom|jzqct=/.jzqsr=bj%2Elianjia%2Ecom|jzqct=/ershoufang/ganluyuan/; gr_user_id=49e91f68-009d-4b8b-8d02-8c31c268cb6b; ljref=pc_sem_baidu_ppzq_x; select_city=110000; all-lj=39e8d71f7d4bc70e2283e0ca888864de; lianjia_ssid=dd7eb92e-f3a7-4ba6-8afe-16c9099af6d2; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1521117506,1521120392,1521438829,1521715567; CNZZDATA1253477573=1723547860-1521113027-%7C1521710379; CNZZDATA1254525948=1604218046-1521114475-%7C1521713755; CNZZDATA1255633284=1458695289-1521112239-%7C1521713824; CNZZDATA1255604082=1607816614-1521112886-%7C1521713827; _jzqa=1.2811990290111634400.1502104083.1521592576.1521715567.18; _jzqc=1; _jzqy=1.1521120393.1521715567.2.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E7%BD%91.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6; _jzqckmp=1; _qzjc=1; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1521715570; _qzja=1.1510458665.1502104082820.1521592576409.1521715567523.1521715567523.1521715570408.0.0.0.95.18; _qzjb=1.1521715567522.2.0.0.0; _qzjto=2.1.0; _jzqb=1.2.10.1521715567.1; _gid=GA1.2.2144421825.1521715572"
#     trans = transCookie(cookie)
#     print trans.stringToDict()





#Testing code
#print get_comhrefs()
#print(temp)
#print(temp[1]['href_community'])