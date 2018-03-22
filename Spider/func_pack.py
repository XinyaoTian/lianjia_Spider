# -*- coding:utf-8 -*-
import json

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
    print list_href
    return list_href

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

if __name__ == "__main__":
    cookie = "lianjia_uuid=7809f78e-b5c2-4047-9bbe-7150bafb1f3d; _smt_uid=59884a12.252f6cd4; _ga=GA1.2.946537891.1502104084; UM_distinctid=16229ab27fe6be-000c12ce97d136-b353461-e1000-16229ab27ff95; Qs_lvt_200116=1521354831; Qs_pv_200116=3112381745763005000%2C3149859735597147600; _jzqx=1.1521357932.1521540918.5.jzqsr=bj%2Elianjia%2Ecom|jzqct=/.jzqsr=bj%2Elianjia%2Ecom|jzqct=/ershoufang/ganluyuan/; gr_user_id=49e91f68-009d-4b8b-8d02-8c31c268cb6b; ljref=pc_sem_baidu_ppzq_x; select_city=110000; all-lj=39e8d71f7d4bc70e2283e0ca888864de; lianjia_ssid=dd7eb92e-f3a7-4ba6-8afe-16c9099af6d2; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1521117506,1521120392,1521438829,1521715567; CNZZDATA1253477573=1723547860-1521113027-%7C1521710379; CNZZDATA1254525948=1604218046-1521114475-%7C1521713755; CNZZDATA1255633284=1458695289-1521112239-%7C1521713824; CNZZDATA1255604082=1607816614-1521112886-%7C1521713827; _jzqa=1.2811990290111634400.1502104083.1521592576.1521715567.18; _jzqc=1; _jzqy=1.1521120393.1521715567.2.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E7%BD%91.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6; _jzqckmp=1; _qzjc=1; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1521715570; _qzja=1.1510458665.1502104082820.1521592576409.1521715567523.1521715567523.1521715570408.0.0.0.95.18; _qzjb=1.1521715567522.2.0.0.0; _qzjto=2.1.0; _jzqb=1.2.10.1521715567.1; _gid=GA1.2.2144421825.1521715572"
    trans = transCookie(cookie)
    print trans.stringToDict()


#Testing code
#print get_comhrefs()
#print(temp)
#print(temp[1]['href_community'])