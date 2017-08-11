#!python3
import requests,os,re
from bs4 import BeautifulSoup
os.chdir(os.getcwd ())
from urllib import request
import urllib.request
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}

url='http://www.xicidaili.com/'


def getdata(url):
    res = requests.get(url, headers=headers)
    res.encoding='utf-8'
    soup =BeautifulSoup(res.text, 'lxml')
#    for chunk in soup.contents(100000): 
#        print(chunk)
    return(soup )
soup=getdata(url)

number=15
content1=soup.find_all('td',limit=number*10)[1::8]
content2=soup.find_all('td',limit=number*10)[2::8]
content5=soup.find_all('td',limit=number*10)[2::8]


#--------------------------------------------------------------------------
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
testurl="http://ip.chinaz.com/"


req = urllib.request.Request(url, headers=header)
resp = urllib.request.urlopen(req, timeout=50)
content = resp.read()

def alive(proxy):
    
    resp=0
    
    proxy_support = urllib.request.ProxyHandler({"http": proxy})
    opener = urllib.request.build_opener(proxy_support)
    
    urllib.request.install_opener(opener)

    req = urllib.request.Request(testurl, headers=header)
    print('尝试连接......')
    try:
        resp = urllib.request.urlopen(req, timeout=50)
        
        
        if resp.status == 200:
            print('连接成功......')

            
            soup = BeautifulSoup(resp,'html.parser',from_encoding='utf-8')
            
            ip=soup.find('p',class_="getlist pl10")
            re1=re.compile(r'</span>(.*?)<span class')
            ip1=re1.findall(str(ip))
            ipp1=ip1[0].strip()
            print(ipp1)
            re2=re.compile(r'<span class="pl10">所在区域：</span>(.*?)<a class')
            ip2=re2.findall(str(ip))            
            ipp2=ip2[0].strip()            
            print(ipp2)
            return(proxy)
    except:
        print('连接失败')
        return False


for i in range(number):
    ip=content1[i].string+':'+content2[i].string

    r=alive(ip)

