#!python3
#@author: the_koala_uncle
#@file:   sougou_weixin_wenzhang.py
#@time:   2017/8/10 9:02
#@desc:   get weixin_wenzhang from sougou

import requests,time,re,os,json
from lxml import etree
os.chdir(os.getcwd())
# a='giKZ97q2-rLJj*Lp-3SbaRoakKk9GYMExakYf6Hl0yPycadNn3tCfyQG*GdzDD77'
# b=''
# signature=a+b
# url='http://mp.weixin.qq.com/profile?src=3&timestamp='+ str(time.time())[0:10] +'&ver=1&signature='+signature
# # DhiEOWmsi8Qqnzv2WCRKGA==
# # g-4Jk*MylHv8M2QYxn95qA==
# # Iavt*GuduKx23KHYB3rCPA==
#
#
# headers={
#     'Host':"mp.weixin.qq.com",
#     'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
#     'Accept':"text/html,application/xhtml+x…lication/xml;q=0.9,*/*;q=0.8",
#     'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#     'Accept-Encoding':"gzip, deflate",
#     'Referer':"http://weixin.sogou.com/weixi…&ie=utf8&_sug_=n&_sug_type_=",
#     'Cookie':"sig=h01826fa4bdd0d0448166293b…9629446de4a088f0d5462acc67cd",
#     'Connection':"keep-alive",
#     'Upgrade-Insecure-Requests':"1",
#     'Cache-Control':"max-age=0"
# }
data=[]
def write(txt):
    with open('list.py','w')as f:
        f.write(txt)
url='http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E5%8D%8A%E6%9C%88%E8%B0%88&ie=utf8&_sug_=n&_sug_type_='

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
}
res=requests.get(url=url,headers=headers)

html=etree.HTML(res.text)
result=html.xpath('id("sogou_vr_11002301_box_0")/div/div[2]/p[1]/a/@href')

url=result[0]
print(url)
res=requests.get(url=url,headers=headers)
##if '验证码'in res.text:
##    print('输入验证码')
##else:
##    geturl=re.compile('"content_url":"(.*?)","copyright_stat"')
##    get_title=re.compile('"title":"(.*?)"}')
##    get_content=re.compile('"digest":"(.*?)",')
##    targeturl_list=geturl.findall(res.text)
##    targettitle_list=get_title.findall(res.text)
##    targetcontent_list=get_content.findall(res.text)
##
##
##    for i in range(len(targeturl_list)):
##        targeturl='http://mp.weixin.qq.com'+targeturl_list[i].replace(';','').replace('ampsrc','src').replace('ampver=1&amp','ver=1&')
##        write(targettitle_list[i])
##        write(targetcontent_list[i])
##        write(targeturl)
##os.startfile('dd.txt')

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


for d in data:
    print(d)
