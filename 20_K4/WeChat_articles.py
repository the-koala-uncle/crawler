#!python3
#@author: the_koala_uncle
#@file:   sougou_weixin_wenzhang.py
#@time:   2017/8/10 9:02
#@desc:   get weixin_wenzhang from sougou

import requests,time,re,os,json,webbrowser
from lxml import etree
os.chdir(os.getcwd())
data=[]

def article(link):

    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
    }
    res=requests.get(url=link,headers=headers)

    html=etree.HTML(res.text)
    result=html.xpath('id("sogou_vr_11002301_box_0")/div/div[2]/p[1]/a/@href')

    url=result[0]

    res=requests.get(url=url,headers=headers)
    try:
        getlist= re.compile('{"app_msg_ext_info":{(.*?)},"comm_msg_info"')
    except:
        webbrowser.open(url)
        input('浏览器中填写认证码')
        getlist= re.compile('{"app_msg_ext_info":{(.*?)},"comm_msg_info"')
    thelist =getlist.findall(res.text)
    for i in range(3):
        the_list= '{'+thelist[i]+'}'
        list=json.loads(the_list,encoding='UTF-8')


        data.append(list["title"])
        data.append(list["digest"])
        url_temp=list["content_url"]
        url_temp = 'http://mp.weixin.qq.com' + url_temp.replace(';', '').replace('ampsrc', 'src').replace('ampver=1&amp', 'ver=1&')
        data.append(url_temp)

        if list["multi_app_msg_item_list"] == '':
            pass
        else:
            n = len(list["multi_app_msg_item_list"])
            for j in range(n):
                data.append(list["multi_app_msg_item_list"][j]["title"])
                data.append(list["multi_app_msg_item_list"][j]["digest"])
                url_temp = list["multi_app_msg_item_list"][j]["content_url"]
                url_temp = 'http://mp.weixin.qq.com' + url_temp.replace(';', '').replace('ampsrc', 'src').replace(
                    'ampver=1&amp', 'ver=1&')
                data.append(url_temp)
def main_art():
    link='http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E5%8D%8A%E6%9C%88%E8%B0%88&ie=utf8&_sug_=n&_sug_type_='
    article(link)
    link='http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E5%8D%97%E9%A3%8E%E7%AA%97&ie=utf8&_sug_=n&_sug_type_='
    article(link)
    listt=[]
    listt=listt+data[:9]+data[30:39]
##    for d in listt:
##        print(d)
    return(listt)
