import requests,os
from bs4 import BeatifulSoup

os.chdir(os.getcwd())
def write():
    with open('Information.txt','a') as f:
        f.write(information+'\r\n')
#headers={        
got=set()
#打印一个
url='http://www.jianshu.com/u/03c9cd05c76d'
res=requests.get(url,headers=headers)
soup=beatifulsoup(res.txt,'lxml')
ids=soup.find('a',class_='name')
ids_name=ids.get_text()
#ids_url=ids['herf'
print(rds)#3
print(rds)#3
print(rds)#3
#3    <a class="name" href="/u/03c9cd05c76d">考拉丶大叔</a>
more=soup.find('div',class_='info')
print(more)
