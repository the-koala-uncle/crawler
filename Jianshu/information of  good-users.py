import requests,os
from bs4 import BeautifulSoup

os.chdir(os.getcwd())
def write(TXT):
    with open('Information.txt','a') as f:
        f.write(TXT+'\r\n')
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {
    'User-Agent': agent
}      
got=set()
number=1
#打印一个
url='http://www.jianshu.com/u/03c9cd05c76d'
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')
ids=soup.find('a',class_='name')
ids_name=ids.get_text()
ids_url='http://www.jianshu.com'+ids['href']
morenum=soup.find('div',class_='info').find_all('p')

moreurl=soup.find('div',class_='info').find('a')['href']

information='（{}）{} ，关注：{} ，粉丝：{} ，收获喜欢：{} ，文章：{} ，总字数：{} ，链接：{}'.format(number,ids_name,morenum[0].get_text(),morenum[1].get_text(),morenum[4].get_text(),morenum[2].get_text(),morenum[3].get_text(),ids_url)
write(information)
