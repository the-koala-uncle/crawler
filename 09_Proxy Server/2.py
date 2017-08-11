import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}

url='http://www.xicidaili.com/wn/'


def getdata(url):
    res = requests.get(url, headers=headers)
    res.encoding='utf-8'
    soup =BeautifulSoup(res.text, 'lxml')
#    for chunk in soup.contents(100000): 
#        print(chunk)
    return(soup )
soup=getdata(url)

number=5
content1=soup.find_all('td',limit=number*10)[1::10]
content2=soup.find_all('td',limit=number*10)[2::10]


def alive1(proxy):
    proxies = { "https": "http://"+proxy}
    print(proxies)
    try:
        res=requests.get(url="https://www.ipip.net/ip.html", proxies=proxies,timeout=30,headers=headers)
        print('666')
 
        print(res.status_code)
#span style="color: rgb(243, 102, 102);">120.239.150.47</span
        a=BeautifulSoup(res.text, "lxml").find_all('span',style="color: rgb(243, 102, 102);")
        print(a)
    except Exception as e:
        print('bad')
        print(e)

def alive(proxy):
    proxies = { "http": "http://"+proxy,"https": "http://"+proxy}
    print(proxies)
    try:
        res=requests.get(url="http://ip.cn/", proxies=proxies,timeout=30)
        print('666')
        print(res.status_code)

        a=BeautifulSoup(res.text, "lxml").find_all('code')
        print(a)
    except Exception as e:
        print('bad')
        print(e)
for i in range(number):
    ip=str(content1[i].string)+str(':')+str(content2[i].string)
    
    r=alive(ip)
