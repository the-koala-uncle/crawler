#!python
#@author: the_koala_uncle
#@file:   get_news.py
#@time:   2017/8/7 8:08
#@desc:   get_news

import requests, os, time, re
from lxml import etree
os.chdir(os.getcwd())
newstxt=''
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}   	

newslist=[]
newsheader=[]
with open('news.txt','w')as f:
        f.write('')

def write(text):
    global newslist
    with open('news.txt','a')as f:
        f.write(text+'\n')
        newslist.append(text)
def writeheader(text):
    global newslist
    with open('news.txt','a')as f:
        f.write(text+'\n')
        newslist.append('header'+str(len(newsheader)))
        newsheader.append(text+'<br>')
        
writeheader(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

#--------------------------新浪新闻-------------------------------------------
url='http://news.sina.com.cn/'
res=requests.get(url,headers=headers)
res.encoding='utf-8'
html = etree.HTML(res.text)
writeheader('新浪新闻：')
            
for i in range(1,10):
    try:
        result = html.xpath('id("syncad_1")/h1['+str(i)+']/a')
        result1 = html.xpath('id("syncad_1")/h1['+str(i)+']/a/@href')
        write(result[0].text)
        write(result1[0])

    except:
        pass
for i in range(1,4):
    for j in range(1,3):
        try:
            result = html.xpath('id("syncad_1")/p['+str(i)+']/a['+str(j)+']')
            result1 = html.xpath('id("syncad_1")/p['+str(i)+']/a['+str(j)+']/@href')
            write(result[0].text)
            write(result1[0])
            
        except:
            pass



#--------------------------澎湃新闻-----------------------------------------
writeheader('澎湃新闻：')

url='http://www.thepaper.cn/'

res=requests.get(url,headers=headers)
res.encoding='utf-8'
html = etree.HTML(res.text)
result=html.xpath('id("clk1756476")')
result_url=html.xpath('id("clk1756476")/@href')
result_content=html.xpath('id("cont1756476")/div[2]/div[1]/p')
##write(result[0].text+ '（' + result_content[0].text + '）')
##write('http://www.thepaper.cn/'+result_url[0])
print(result_content)
result=html.xpath('//div[@class="news_li"]/div[1]/a[1]/img/@alt')
result_url=html.xpath('//div[@class="news_tu"]/a/@href')
result_content=html.xpath('//div[@class="news_li"]/p')
for i in range(10):
    write(result[i]+ '（' + result_content[i].text + '）')
    write('http://www.thepaper.cn/'+result_url[i])


#--------------------------构造网页-------------------------------------------
html1 = """ 
<html> 
  <head></head> 
  <body> 
    <p>Hi!It's time for news!<br>  
"""
html2=newsheader[0]
for n in range(0,len(newslist)-1,2):
    if newslist[n][0:5]=='header':
        html2=html2+newsheader[newslist[n][6:]]+'<br>'
    else:      
        html2 =html2+'<a href="'+newslist[n+1]+'">'+newslist[n]+'</a><br>' 
html3=""" 
    </p> 
  </body> 
</html>
"""
html=html1+html2+html3

#---------------------------发邮件-------------------------------------------
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
sender_qq = '1433289097'
#pwd为qq邮箱的授权码
pwd = 'emgpxziezpxqicdg'
#发件人的邮箱
sender_qq_mail = '1433289097@qq.com'
#收件人邮箱
receiver = '1433289097@qq.com'
#邮件的正文内容
mail_content = html
#newstxt
#邮件标题
mail_title = 'News (autosend by python)'

#ssl登录
smtp = SMTP_SSL(host_server)
#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(0)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "html", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
print('已发送')
#只需要更改host_server 、sender_qq、pwd、sender_qq_mail、receiver、mail_content、mail_title等数据，就可以实现简单的发送任务。
#MIMEText函数中的第二个参数为“plain”时，发送的是text文本。如果为“html”，则能发送网页格式文本邮件。

#os.startfile('news.txt')
