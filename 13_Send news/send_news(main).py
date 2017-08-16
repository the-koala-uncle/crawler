#!python
#@author: the_koala_uncle
#@file:   get_news.py
#@time:   2017/8/7 8:08
#@desc:   get_news

import requests, os, time, re
from lxml import etree

from 126email import send_email

os.chdir(os.getcwd())




headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}   	

newslist=[]

def write(list):
    global newslist
##    with open('news.txt','a')as f:
##        if type(list)==type([]):
##            f.write(list[0]+'\n'+list[0]+'\n')            
##        else:
##            f.write(list+'\n')
    newslist.append(list)

        
write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

#--------------------------新浪新闻-------------------------------------------
url='http://news.sina.com.cn/'
res=requests.get(url,headers=headers)
res.encoding='utf-8'
html = etree.HTML(res.text)
write('<h2>新浪新闻：</h2>')
            
for i in range(1,10):
    try:
        result = html.xpath('id("syncad_1")/h1['+str(i)+']/a')
        result1 = html.xpath('id("syncad_1")/h1['+str(i)+']/a/@href')
        write([result[0].text,esult1[0]])

    except:
        pass
for i in range(1,10):#调新闻数量
    for j in range(1,3):
        try:
            result = html.xpath('id("syncad_1")/p['+str(i)+']/a['+str(j)+']')
            result1 = html.xpath('id("syncad_1")/p['+str(i)+']/a['+str(j)+']/@href')
            write([result[0].text,result1[0]])            
        except:
            pass


#--------------------------澎湃新闻-----------------------------------------
write('<h2>澎湃新闻：</h2>')
url='http://www.thepaper.cn/'
res=requests.get(url,headers=headers)
res.encoding='utf-8'
html = etree.HTML(res.text)

result=html.xpath('//div[@class="pdtt_rt"]/div[1]/div[1]/a')
result_url=html.xpath('//div[@class="pdtt_rt"]/div[1]/div[1]/a/@href')
result_content=html.xpath('//div[@class="pdtt_rt"]/div[1]/p')

write([result[0].text,'http://www.thepaper.cn/'+result_url[0],result_content[0].text])

      
result=html.xpath('//div[@class="news_li"]/div[1]/a[1]/img/@alt')
result_url=html.xpath('//div[@class="news_tu"]/a/@href')
result_content=html.xpath('//div[@class="news_li"]/p')

for i in range(8):#调新闻数量
    write([result[i],'http://www.thepaper.cn/'+result_url[i],result_content[i].text])
    
#--------------------------构造网页-------------------------------------------
html1 = """ 
<html> 
  <head></head> 
  <body> 
    <p>Hi!It's time for news!<br>  
"""
html2 =''
for n in range(0,len(newslist)-1):
    if type(newslist[n])==type([]):
        if str(len(newslist[n]))=='3':
            html2 =html2+'<a href="'+newslist[n][1]+'">'+newslist[n][0]+'</a><br>'
            html2 =html2+newslist[n][2]+'<br>'
        else:
            html2 =html2+'<a href="'+newslist[n][1]+'">'+newslist[n][0]+'</a><br>'
    else:      
        html2 =html2+newslist[n] 
html3=""" 
    </p> 
  </body> 
</html>
"""
html=html1+html2+html3

with open('news.html','w')as f:
        f.write(html)
os.startfile('news.html')
#--------------------------send email-------------------------------------------


send_mail()

