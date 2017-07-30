#python3

import requests,os,re

os.chdir (os.getcwd ())

agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent': agent}

url1='http://ris.szpl.gov.cn/credit/showcjgs/ysfcjgs.aspx?cjType=1'

def getdata(url):
    res=requests.get(url,headers =headers )
    one=re.compile(r'<td align="right" style="border-color:#DEEFF5;">(.*?)</td>')
    one1=re.compile(r'<SPAN class=titleblue><span id="lblCurTime3">(.*?)</span>')


    content1=one1.findall (res.text)
    content=one.findall (res.text)


    a=str(content[-3])
    b=str(content[-2])
    a=a.rstrip()
    b=b.rstrip()

    out=str(content1[0])+' 一手房成交深圳（全市）商品住房成交信息：成交面积为：'+ a +'(㎡)，成交均价：'+ b +'(元) '
    print(out)

getdata(url1)

#2017年06月 一手房成交深圳（全市）商品住房成交信息：成交面积为：292342.01(㎡)，成交均价：54492(元)
