#！python3
#Download the latest haizeiwang_manhua

import requests,os,bs4
from lxml import etree
mainurl = 'http://op.hanhande.com'
os.makedirs('manhua',exist_ok=True)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

#find the new manhua
print('Downloading page %s...' % mainurl)
res = requests.get(mainurl,headers=headers)
res.encoding='gb2312'
print(res.status_code)

html=etree.HTML(res.text)
result=html.xpath('id("main")/div[2]/div[1]/div[3]/ul[1]/li[1]/cite/a')
print('最新一集海贼王漫画是：'+result[0].text)
input('回车继续下载，否则请关闭窗口')

#soup = bs4.BeautifulSoup(res.text, "lxml")
#newlink=soup.select('.newsbox a[rel="nofollow"]')
result=html.xpath('id("main")/div[2]/div[1]/div[3]/ul[1]/li[1]/cite/a/@href')
newlink=result[0]
print('Find the new web is : '+newlink)
num=0
#save manhua
while newlink!=[]:
    num=num+1
    print('Downloading page NO.%s...' % num) 
    res = requests.get(newlink) 
    res.raise_for_status() 
    soup = bs4.BeautifulSoup(res.text, "lxml") 
    picture = soup.select('#pictureContent img') 
    if picture == []: 
        print('Could not find comic image.') 
    else: 
        pictureUrl =picture[0].get('src') 
     # Download the image. 
        print('Downloading image NO.%s...' % num) 
        res = requests.get(pictureUrl) 
        res.raise_for_status() 
     
    # Save the image 
        imageFile = open(os.path.join('manhua', os.path.basename(pictureUrl)), 'wb') 
    for chunk in res.iter_content(100000): 
        imageFile.write(chunk) 

    #page__next
    newlink = soup.select('#page__next a')
    if newlink!=[]:
        newlink=newlink[0].get('href')  
imageFile.close() 
print('Done.')                    
