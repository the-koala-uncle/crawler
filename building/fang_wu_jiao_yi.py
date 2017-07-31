#python3

import requests,os,re

os.chdir (os.getcwd ())

agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent': agent}



def getdata1():
    url='http://ris.szpl.gov.cn/credit/showcjgs/ysfcjgs.aspx?cjType=1'
    res=requests.get(url,headers =headers )
    one=re.compile(r'<td align="right" style="border-color:#DEEFF5;">(.*?)</td>')
    one1=re.compile(r'<SPAN class=titleblue><span id="lblCurTime3">(.*?)</span>')
    content1=one1.findall (res.text)
    content=one.findall (res.text)
    a=str(content[-3])
    b=str(content[-2])
    time=str(content1[0])
    a=a.rstrip()
    b=b.rstrip()
    return(time,a,b)



def getdata2():
    url='http://ris.szpl.gov.cn/credit/showcjgs/esfcjgs.aspx'
    res=requests.get(url,headers =headers )
    two=re.compile(r'<td align="right" style="border-color:#DEEFF5;">(.*?)</td>')
    content=two.findall(res.text)
    b=str(content[6])
    b=b.rstrip()
    return(b)

def start():
    time,a1,a2=getdata1()
    b1=getdata2()

    print(time+'深圳（全市）商品住房成交信息:')
    print('一手房成交面积为：'+ a1 +'(㎡)，+成交均价：'+ a2 +'(元/㎡) ')
    print('二手房住宅成交面积为：'+ b1 +'(㎡)')

start()

'''
2017年06月深圳（全市）商品住房成交信息:
一手房成交面积为：292342.01(㎡)，+成交均价：54492(元/㎡) 
二手房住宅成交面积为：540008.22(㎡)

'''
