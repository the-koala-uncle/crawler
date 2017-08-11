#!python3
#the sample for web_spider
import requests,os,time
from bs4 import BeautifulSoup
from collections import deque
os.chdir(os.getcwd ())


#---------------------------------日志---------------------------------------------

from random import choice
import logging
#打印日志
#logging.basicConfig(filename='log.txt', level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#禁用日志
#logging.disable(logging.DEBUG)

#---------------------------------网址---------------------------------------------
url=''
url1=''
url2=''
#----------------------------------模拟表头---------------------------------------------
def get_headers():
    #搜狗浏览器 1.x
    Agent1='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
    #360浏览器
    Agent2='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'

    #IE 11
    Agent3='Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'

    #Android QQ浏览器 For android
    Agent4='MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'

    headers={
        'User-Agent':Agent2
        }
    return(headers)

#------------------------------------------------------------------------------

#----------------------------------获取代理--------------------------------------------
def get_proxy(number=5):
    #从XiciDaili.com获取国内高匿代理IP
    Deque=deque()
    headers = get_headers()
    res = requests.get('http://www.xicidaili.com/nn/', headers=headers)
    soup =BeautifulSoup(res.text, 'lxml')


    content1=soup.find_all('td',limit=number*10)[1::10]
    content2=soup.find_all('td',limit=number*10)[2::10]
    content3=soup.find_all('td',limit=number*10)[8::10]
    content4=soup.find_all('div',class_='bar',limit=number*10)[0::2]
    for i in range(number):
        logging.debug('代理测试中......')
        ip=content1[i].string + ':' + content2[i].string
        livetime=content3[i].string
        speed=content4[i].get('title')

    #判断是否满足使用要求
        if float(speed[0:-1])>1.3:
            # 调时间，单位是秒
            logging.debug('the one is unuseful,code=1')
            continue
        else:
            pass

        if livetime[-1]=='天':
            t=int(livetime[0:-1])*24*60
        elif livetime[-1]=='时':
            t=int(livetime[0:-2])*60
        elif livetime[-1]=='钟':
            t=int(livetime[0:-2])
        else:
            t=0
        if t<10:
            #调iP可以使用时限，单位是分钟
            logging.debug('the one is unuseful,code=2')
            continue
        else:
            pass
        

    #连接网络检验       
        proxies = { "http": "http://"+ip,"https": "http://"+ip}
    
        try:
            res=requests.get(url="http://ip.cn/", proxies=proxies,timeout=30,headers=headers)
            if res.status_code == 200:
                ip_address=BeautifulSoup(res.text, "lxml").find_all('code')

                if ip_address[0].string == content1[i].string:
                    logging.debug('got one :')
                    logging.debug( proxies)
                    Deque.append(proxies)
                else:
                    logging.debug('the one is unusefu,code=5')
            else:
                logging.debug('res.status_code='+str(res.status_code))
                logging.debug('the one is unusefu,code=4')
      
        except Exception as e:
            logging.debug('the one is unuseful,code=3')
            #print('wrong at proxies_test')
            #print(e)
        

        time.sleep(1)
    print('成功获取IP数：'+str(len(Deque)))
    return(Deque)
#------------------------------------------------------------------------------

#----------------------------------请求网页数据------------------------------------------
def get_webdata(url,headers):
    try:
        res=requests.get(url,headers=headers)
        #res.encoding='GB2313'
        return(res)
    except Exception as e:
        print('wrong at get_webdata!')
        print(e)
#-----------------------------------解析数据-------------------------------------------

#------------------------------------------------------------------------------
if __name__ == '__main__':
    print('--------------spider start---------------')
    proxies=[]

    #是否使用代理
#    proxylist=get_proxy(number=4)

    try:
        proxies=choice(proxylist)
    except:
        pass

    headers = get_headers()
 #   res=requests.get(url, proxies=proxies,headers=headers)
#------------------------------------------------------------------------------

    res=requests.get(url="http://ip.cn/", proxies=proxies,timeout=30,headers=headers)
    if res.status_code == 200:
        ip_address=BeautifulSoup(res.text, "lxml").find_all('code')


    print(ip_address)
