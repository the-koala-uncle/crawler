
# coding: utf-8

# In[1]:

#!python3
#sign in zhihu
import requests,os,time,re,sys
from PIL import Image
from http import cookiejar
from bs4 import BeautifulSoup
os.chdir(os.getcwd())
#添加表头
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'
}


# In[2]:

#Cookie数据加载
session=requests.session()
session.cookies=cookiejar.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")


# In[3]:

#获取xsrf码
def get_xsrf(url):
    #url = 'https://www.zhihu.com/#signin'
    url_xsrf=url+'/#signin'
    req=requests.get(url_xsrf,headers=headers)
    soup=BeautifulSoup(req.content,'html.parser')
    try:
        xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
    except:
        xsrf = ''
    return xsrf


# In[4]:

#获取验证码
def get_captcha(url):
#'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"   
    t=str(int(time.time()*1000))
    captcha_url = url+'/captcha.gif?r=' + t + "&type=login"
    req_captcha=session.get(captcha_url,headers=headers)
    with open('captcha.jpg','wb')as f:
        f.write(req_captcha.content)
    try:
        im=Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        os.startfile('')
    captcha=input('输入验证码：')
    return captcha


# In[5]:

def signin(account,password):
    _xsrf = get_xsrf(url)
  #  headers["X-Xsrftoken"] = _xsrf
   # headers["X-Requested-With"] = "XMLHttpRequest"
    # 通过输入的用户名判断是否是手机号
    if re.match(r"^1\d{10}$", account):
        print("手机号登录 \n")
        post_url = 'https://www.zhihu.com/login/phone_num'
        data = {
            '_xsrf': _xsrf,
            'password': password,
            'phone_num': account
        }
    else:
        if "@" in account:
            print("邮箱登录 \n")
            
        else:
            print("你的账号输入有问题，请重新登录")
            return 0
        post_url = 'https://www.zhihu.com/login/email'
        data = {
            '_xsrf': _xsrf,
            'password': password,
            'email': account
        }
    # 不需要验证码直接登录成功
    login_page = session.post(post_url, data=data, headers=headers)
    login_code = login_page.json()
    if login_code['r'] == 1:
        # 不输入验证码登录失败
        # 使用需要输入验证码的方式登录
        captcha=get_captcha(url)
        data["captcha"] = captcha
        login_page = session.post(post_url, data=data, headers=headers)
        login_code = login_page.json()
        print(login_code['msg'])
        session.cookies.save()


# In[6]:

# 通过查看用户个人信息来判断是否已经登录
def isLogin():   
    url = "https://www.zhihu.com/settings/profile"
    login_code =session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False


# In[7]:

try:
    input = raw_input
except:
    pass
if __name__ == '__main__':
    url='https://www.zhihu.com' 
    if isLogin():
        print('您已经登录')
    else:
       # account = input('请输入你的用户名\n>  ')
        #password = input("请输入你的密码\n>  ")
        account = ''
        password = ''
        signin(account,password)

