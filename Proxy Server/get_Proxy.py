#!python3
#get Proxy

import os,requests
from bs4 import BeautifulSoup
from collections import deque
num=0
#class getProxy():

def getone(cla):
    url='http://www.xicidaili.com/nn/'
    headers={    
        'Host':'www.xicidaili.com',
        'Referer':'http://www.so.com/link?m=aPh8cfhKQ2NFc1RnOMWh5a7QC3YM7q5XuBGmyxUXTySoLTq0kmNWg8UN8kM5wC0%2Bu695HB4%2FdearMLWKRvF7xUQKAWXc5tZBALokisY82c%2FhO%2BvCXgOHaTetN06GBGCHnwXJcgQUJQk0%3D',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        }
    global num
    num=num+1
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')
    content1=soup.find('tr',class_='odd').findAll('td')
    content11=soup.find('tr',class_='odd').findAll('div',class_='bar')
    for s in content11:
        content11[content11.index(s)]=s.get('title')
   
    for n in content1:
        content1[content1.index(n)]=(n.get_text().strip())

    content1[6],content1[7]=content11[0],content1[1]
    content1[0]=num
    print(content1)

def getProxy(number):
    Deque=deque()
    url='http://www.xicidaili.com/nn/'
    headers={    
        'Host':'www.xicidaili.com',
        'Referer':'http://www.so.com/link?m=aPh8cfhKQ2NFc1RnOMWh5a7QC3YM7q5XuBGmyxUXTySoLTq0kmNWg8UN8kM5wC0%2Bu695HB4%2FdearMLWKRvF7xUQKAWXc5tZBALokisY82c%2FhO%2BvCXgOHaTetN06GBGCHnwXJcgQUJQk0%3D',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        }
    print('00000000000000000')
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')
    content1=soup.find_all('td',limit=number*10)[1::10]
    content2=soup.find_all('td',limit=number*10)[2::10]
    content3=soup.find_all('td',limit=number*10)[8::10]
    content4=soup.find_all('div',class_='bar',limit=number*10)[0::2]

    for i in range(number):
        Deque.append(content1[i].string)
        Deque.append(content2[i].string)       
        Deque.append(content4[i].get('title'))
        Deque.append(content3[i].string)
    return(Deque)

print(getProxy(5))
#d.popleft()
