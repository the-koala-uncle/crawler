#!python3
#get Proxy

import requests,re
from bs4 import BeautifulSoup
from collections import deque

url='http://ip.chinaz.com/'

headers={
    'Host':'ip.chinaz.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }


ip='183.189.185.231'
port='80'
ht='http'


proxies={ ht :'http//'+ip+':'+port}



try:
    res=requests.get(url,headers=headers,proxies=proxies)
    ree=re.compile(r'</span>(.*?)<span class')
    ipp=ree.findall(res.text)
    ipre=ipp[0].strip()
    if ipre=='116.7.28.58':
        print('本机ip')
    else:
        print(ipre)
except Exception as e: 
    print('Not working......')
    print(e)

