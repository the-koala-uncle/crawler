import requests,os,time
from bs4 import BeautifulSoup
from collections import deque
os.chdir(os.getcwd())
from math import ceil

got=set()
Deque=deque(maxlen=50)

number=1
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent': agent} 


def write(TXT):
    with open('Information.txt','a') as f:
        f.write(TXT+'\r\n')


def get_one(url):
    global number 
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')
    ids=soup.find('a',class_='name')
    ids_name=ids.get_text()
    ids_url='http://www.jianshu.com'+ids['href']
    morenum=soup.find('div',class_='info').find_all('p')
    for q in range(len(morenum)):
        morenum[q]=morenum[q].get_text()
    moreurl=soup.find('div',class_='info').find('a')['href']
    moreurl='http://www.jianshu.com'+moreurl
    information='（{}）{} ，关注：{} ，粉丝：{} ，收获喜欢：{} ，文章：{} ，总字数：{} ，链接：{}'.format(number,ids_name,morenum[0],morenum[1],morenum[4],morenum[2],morenum[3],ids_url)
    number=number+1
    write(information)
    print(information)
    return(moreurl,morenum[0])


def morelist(url,page):
    pagenum=ceil(int(page)/9)
    for n in range(1,1+pagenum):
        newurl=url+'?page='+str(n)
        res=requests.get(newurl,headers=headers)
        soup=BeautifulSoup(res.text,'lxml')
        idd=soup.find('div',id='list-container').findAll('a',class_='name')
       # idd_name=[]
        idd_url=[]
        for q in range(len(idd)):
            #idd_name.append(idd[q].get_text())
            idd_url.append('http://www.jianshu.com'+idd[q]['href'])
        Deque.extend(idd_url) 
        time.sleep(1)


def start():
    while Deque!=[]:
        url=Deque.popleft()
        if url not in got:
            got.add(url)
            moreurl,page=get_one(url)
            morelist(moreurl,page)


if __name__=='__main__':
    Deque.append('http://www.jianshu.com/u/03c9cd05c76d')
    start()
