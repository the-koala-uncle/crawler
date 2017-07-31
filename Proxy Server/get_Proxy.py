#!python3
#get Proxy

import requests
from bs4 import BeautifulSoup
from collections import deque

url='http://www.xicidaili.com/nn/'
headers={    
    'Host':'www.xicidaili.com',
    'Referer':'http://www.so.com/link?m=aPh8cfhKQ2NFc1RnOMWh5a7QC3YM7q5XuBGmyxUXTySoLTq0kmNWg8UN8kM5wC0%2Bu695HB4%2FdearMLWKRvF7xUQKAWXc5tZBALokisY82c%2FhO%2BvCXgOHaTetN06GBGCHnwXJcgQUJQk0%3D',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }

#获取ip
def getProxy(number):
    Deque=deque()
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')
    content1=soup.find_all('td',limit=number*10)[1::10]
    content2=soup.find_all('td',limit=number*10)[2::10]
    content3=soup.find_all('td',limit=number*10)[8::10]
    content4=soup.find_all('div',class_='bar',limit=number*10)[0::2]


    for i in range(number):
        if judge(content4[i].get('title'),content3[i].string):
            one=[content1[i].string,content2[i].string,content4[i].get('title'),content3[i].string]
            Deque.append(one)
            print('Get one.........')
        else:
            print('Delete one......')
    return(Deque)

#判断是否满足使用要求
def judge(speed,tim):
    if float(speed[0:-1])>1.3:    # 调时间，单位是秒
        return(False)
    else:
        pass

    if tim[-1]=='天':
        t=int(tim[0:-1])*24*60
    elif tim[-1]=='时':
        t=int(tim[0:-2])*60
    elif tim[-1]=='钟':
        t=int(tim[0:-2])
    else:
        t=0
    if t<10:                 #调iP可以使用时限，单位是分钟
        return(False)
    else:
        pass
    return(True)

#连接网络检验
def test(ip,port,wait):
    timeout=wait
    proxies={'http':'http//'+ip+':'+port,'https':'https//'+ip+':'+port}

    url1='http://www.qq.com'
    try:
        res=requests.get(url,headers=headers,proxies=proxies,verify=False,timeout=timeout)       
        print(res.status_code)
    except:
        print('Not working......')
    

def start(numm,wait):   
    got=getProxy(numm)
    print('-----------------------')
    print('Testing ip now...')
    for e in got:
        test(e[0],e[1],wait)
#d.popleft()
start(5,60)
