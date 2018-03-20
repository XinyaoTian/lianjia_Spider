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
            list_href.append(item["href_community"])
    #print list_href
    return list_href

#get_comhrefs()


#Testing code
#print get_comhrefs()
#print(temp)
#print(temp[1]['href_community'])