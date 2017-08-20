#!python
#@author: the_koala_uncle
#@file:   get_news.py
#@time:   2017/8/7 8:08
#@desc:   get_news

import requests, os, time, re, configparser
from lxml import etree
from WeChat_articles import main_art

os.chdir(os.getcwd())


def news():

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}   	

    newslist=[]

            
    newslist.append(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print('开始爬取资源')
    #--------------------------新浪新闻-------------------------------------------
    url='http://news.sina.com.cn/'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    html = etree.HTML(res.text)
    newslist.append('<h2>新浪新闻：</h2>')
                
    for i in range(1,10):
        try:
            result = html.xpath('id("syncad_1")/h1['+str(i)+']/a')
            result1 = html.xpath('id("syncad_1")/h1['+str(i)+']/a/@href')
            newslist.append([result[0].text,esult1[0]])

        except:
            pass
    for i in range(1,10):#调新闻数量
        for j in range(1,3):
            try:
                result = html.xpath('id("syncad_1")/p['+str(i)+']/a['+str(j)+']')
                result1 = html.xpath('id("syncad_1")/p['+str(i)+']/a['+str(j)+']/@href')
                newslist.append([result[0].text,result1[0]])            
            except:
                pass


    #--------------------------澎湃新闻-----------------------------------------
    newslist.append('<h2>澎湃新闻：</h2>')
    url='http://www.thepaper.cn/'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    html = etree.HTML(res.text)

    result=html.xpath('//div[@class="pdtt_rt"]/div[1]/div[1]/a')
    result_url=html.xpath('//div[@class="pdtt_rt"]/div[1]/div[1]/a/@href')
    result_content=html.xpath('//div[@class="pdtt_rt"]/div[1]/p')

    newslist.append([result[0].text,'http://www.thepaper.cn/'+result_url[0],result_content[0].text])

          
    result=html.xpath('//div[@class="news_li"]/div[1]/a[1]/img/@alt')
    result_url=html.xpath('//div[@class="news_tu"]/a/@href')
    result_content=html.xpath('//div[@class="news_li"]/p')

    for i in range(8):#调新闻数量
        newslist.append([result[i],'http://www.thepaper.cn/'+result_url[i],result_content[i].text])
    #--------------------------微信公众号-----------------------------------------
    newslist.append('<h2>半月谈和南风窗：</h2>')
    temp_list=main_art()
    for i in range(0,len(temp_list),3):
        newslist.append([temp_list[i],temp_list[i+2],temp_list[i+1]])

    #--------------------------软件应用-------------------------------------------
    try:
        url='http://www.wandoujia.com/?utm_source=wx_baidu&utm_medium=cpc&utm_term=%E8%B1%8C%E8%B1%86%E8%8D%9Aapp%E4%B8%8B%E8%BD%BD&utm_content=%E6%A0%B8%E5%BF%83%E8%AF%8D&utm_campaign=wdjpzbt'
        res=requests.get(url,headers=headers)
        res.encoding='utf-8'
        html = etree.HTML(res.text)
        newslist.append('<h2>软件应用：</h2>')

        result = html.xpath('//div[@class="review-content"]/a')
        result1 = html.xpath('//p[@class="review-desc"]')

        for i in range(3):
            newslist.append([result[i].text.replace(' ','').replace('\n',''),result[i].get('href'),result1[i].text])


    except:
        print('软件应用1')

    url='http://zuimeia.com/apps/?platform=2'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    html = etree.HTML(res.text)
    result = html.xpath('//div[@class="article-title"]/a/h1')
    result1 = html.xpath('//a[@class="quote-text"]')
    for i in range(3):
        newslist.append([result[i].text,'http://zuimeia.com'+result1[i].get('href'),result1[i].text])


       
    #--------------------------构造网页-------------------------------------------
    html1 = """ 
    <html> 
      <head></head> 
      <body> 
        <p>Hi! It's time for news!<br>  
    """
    html2 =''
    for n in range(0,len(newslist)):
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

##    with open('news.html','w')as f:
##        f.write(html.encode("gbk","ignore").decode("gbk"))
    return(html)
#--------------------------send email-------------------------------------------
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
def send_mail(plain,aa,bb,cc,dd):
# 接收参数: 发件人地址
    from_addr =aa

    # 接收参数: 客户端授权密码
    passwd = bb

    # 接收参数: 收件人地址,可多个
    to_addrs =cc

    # 接收参数: SMTP服务器(注意:是发件人的smtp服务器)
    smtp_server = dd


    # 接收参数: 邮件主题
    subject = '每日一闻'

    # 接收参数: 邮件正文
   # plain = '我用python!'

    # 带附件邮件
    # 指定subtype为alternative，同时支持html和plain格式
    msg = MIMEMultipart('alternative')
    # 邮件正文中显示图片，同时附件的图片将不再显示
    # plain = 'Hello world and hello me!'
    msg.attach(MIMEText(str(plain), 'html', 'utf-8'))       # 纯文本
    # html = '<html><body><h1>Hello</h1><p><img src="cid:0"></p></body></html>'
    # msg.attach(MIMEText(html, 'html', 'utf-8'))         # HTML
    # msg=(MIMEText(html, 'html', 'utf-8'))         # HTML 可以用
    # 添加附件：即关联一个MIMEBase，图片为本地读取
    

    # 未指定用户别名，则客户端会自动提取邮件地址中的名称作为邮件的用户别名
    msg['From'] = _format_addr(from_addr)
    # msg['To'] = _format_addr(to_addrs)
    msg['To'] = '%s' % ','.join([_format_addr('<%s>' % to_addr)
                                 for to_addr in to_addrs])
    msg['Subject'] = Header(str(subject), 'utf-8').encode()
    msg['Date'] = formatdate()


    #=========================================================================
    # 发送邮件
    #=========================================================================
    try:
        # SMTP服务器设置(地址,端口):
        server = smtplib.SMTP_SSL(smtp_server, 465)
        # server.set_debuglevel(1)
        # 连接SMTP服务器(发件人地址, 客户端授权密码)
        server.login(from_addr, passwd)

        # 发送邮件
        server.sendmail(from_addr, to_addrs, msg.as_string())

        print('邮件发送成功')

    except smtplib.SMTPException as e:
        print(e)
        print('邮件发送失败')

    finally:
        # 退出SMTP服务器
        server.quit()




def main_news(data):
    config = configparser.ConfigParser()
    config.read(data)
    user = config.get('emailbox','user')
    psw = config.get('emailbox','psw')
    smtp = config.get('emailbox','smtp')
    html=news()
    send_mail(html,user,psw,user,smtp)
#os.startfile('news.html')
