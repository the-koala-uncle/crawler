 #!python3
#the sample for web_spider
import requests,os,time,re
from bs4 import BeautifulSoup
from collections import deque
from http import cookiejar

#---------------------------------日志---------------------------------------------

from random import choice
import logging
#打印日志
#logging.basicConfig(filename='log.txt', level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#禁用日志
logging.disable(logging.DEBUG)


#-------------------------------模拟表头---------------------------------------------
def get_headers():
    #搜狗浏览器 1.x
    Agent1='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
    #360浏览器
    Agent2='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'

    #IE 11
    Agent3='Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'

    #Android QQ浏览器 For android
    Agent4='MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'

    headers={
        'User-Agent':Agent2
        }
    return(headers)

#-------------------------------Cookie数据-----------------------------------------------
def use_cookies():
    session=requests.session()
    session.cookies=cookiejar.LWPCookieJar(filename='cookies')
    try:
        session.cookies.load(ignore_discard=True)
    except:
        print("Cookie 未能加载")

    login_page = session.post(post_url, data=data, headers=headers)
        
    session.cookies.save()
#-------------------------------获取代理--------------------------------------------
def is_or_not_proxy(n):
    if n==0:
        proxies=[]
        return(proxies)
    if n==1:
        try:
            proxies=choice(get_proxy())
            return(proxies)
        except:
            print('未能使用代理')
            proxies=[]
            return(proxies)

def get_proxy(number=30):
    #从XiciDaili.com获取国内高匿代理IP
    Deque=deque()
    headers = get_headers()
    res = requests.get('http://www.xicidaili.com/nn/', headers=headers)
    soup =BeautifulSoup(res.text, 'lxml')


    content1=soup.find_all('td',limit=number*10)[1::10]
    content2=soup.find_all('td',limit=number*10)[2::10]
    content3=soup.find_all('td',limit=number*10)[8::10]
    content4=soup.find_all('div',class_='bar',limit=number*10)[0::2]
    for i in range(number):
        if len(Deque)>4:
            continue
        print('代理测试中......')
        ip=content1[i].string + ':' + content2[i].string
        livetime=content3[i].string
        speed=content4[i].get('title')

    #判断是否满足使用要求
        if float(speed[0:-1])>1.3:
            # 调时间，单位是秒
            logging.debug('the one is unuseful,code=1')
            continue
        else:
            pass

        if livetime[-1]=='天':
            t=int(livetime[0:-1])*24*60
        elif livetime[-1]=='时':
            t=int(livetime[0:-2])*60
        elif livetime[-1]=='钟':
            t=int(livetime[0:-2])
        else:
            t=0
        if t<10:
            #调iP可以使用时限，单位是分钟
            logging.debug('the one is unuseful,code=2')
            continue
        else:
            pass
        

    #连接网络检验       
        proxies = { "http": "http://"+ip,"https": "http://"+ip}
    
        try:
            res=requests.get(url="http://ip.cn/", proxies=proxies,timeout=30,headers=headers)
            if res.status_code == 200:
                ip_address=BeautifulSoup(res.text, "lxml").find_all('code')

                if ip_address[0].string == content1[i].string:
                    logging.debug('got one :')
                    logging.debug( proxies)
                    Deque.append(proxies)
                else:
                    logging.debug('the one is unusefu,code=5')
            else:
                logging.debug('res.status_code='+str(res.status_code))
                logging.debug('the one is unusefu,code=4')
      
        except Exception as e:
            logging.debug('the one is unuseful,code=3')
            #print('wrong at proxies_test')
            #print(e)
        

        time.sleep(1)
        
            
    print('成功获取IP数：'+str(len(Deque)))
    return(Deque)

#----------------------------------请求网页数据------------------------------------------
def get_webdata(url,headers):
    try:
        res=requests.get(url,headers=headers)
        #res.encoding='GB2313'
        return(res)
    except Exception as e:
        print('wrong at get_webdata!')
        print(e)
#-----------------------------------解析数据-------------------------------------------
'''                                                                              
                                                                                
                                     $$$$                                       
                               $$d0x0o#uxx0z#$$                                 
                            $WcxxxxW   "kx}  "hd$                               
                          $qxxxxxxJ     "c     Wxd$                             
                        $#xxxxxxxch      #      cxu$                            
                       $uxxxxxxxxk>    p"-  h}  #xxxB                           
                     $0xxxxxxxxxx#    # n "h I# nxxxx$                          
                    $Yxxxxxxxxxxx#    I  }C     -qcxxx$                         
                   $Yxxxxxxxxxxxq#(      "-     z  -occ$                        
                   $xxxxxxxxxxc#(Ip      ( COC( h    pu$                        
                  $xxxxxxxxxuh    ">     n}p zk8"     "8$$$                     
                  mxxxxxxxxk"      >C  ff &\  kk    }#>#   $                    
                 $xxxxxxxx# -Cp}          ok\kkk> C(       "$                   
                 cxxxxxxxW       }zh(     @kkkko >          $                   
                $xxxxxxxq             }h   8kko(            p                   
                mxxxxxxx>                    -    #pnf----I p                   
               $xxxxxxuW   >nn---I           O              $                   
               $xxxxxx#"              ->     p             I                    
               Wxxxxxx>                      n-   OhnI     $                    
               qxxxxx0     }&%%%pOn}I  ((    -n        }Oh$                     
               Jxxxxx#    "kkkkkkka8%*aW%pn- -n        }CI$                     
               Jxxxxxp    -kkkkkWB8akkkkkkoWBhp}I    >z#  $                     
               cxxxxx}    nk*%okkkkkkkkkkkkkkkkkkkkkkkk"  $                     
               Jxxxxx     nkkkkkkkkkkkkkkkkkkkkkkkkkkk%   $                     
               Jxxxxx     Ikkkkkkkkkkkkkkkkkkkkkkkkkkk-                         
               qxxxxx      akkkkkkkkkkkkkkkkkkkkkkkkkB   f                      
               Wxxxxx      8kkkaW%8#kkkkkkkkkkkkkkkkh"   8                      
               $xxxxx      Ik&YffffffQBhkkkkkkkkkkkkO   z$                      
               $xxxxx(      $ffffffffffx@kkkkkkkkkkB    $                       
                mxxxx#      "ufffffffffffbkkkkkkkk#    I                        
                $xxxxY       nffffffffffffMkkkkkka"    8                        
                 uxxxxf       hffffffffffffWkkkka>    I                         
                 qxxxx#       "Qfffffffffff%kkkkW     O                         
                 $xxxxcp       "bffffffffffckkk8     "$                         
                  dxxxxc         omfffffffffa8C      $                          
                  $xxxxxW          CQffffffQz       8                           
                   $xxxxx}           >hbpo(        8                            
                    #xxxxY"      -(O%$}  IBkkkkkkkoB                            
                     0xxxx0 >O%*kkkkB      k#j>Ij#kk$                           
                     $Jxxm8akkkkoWW&"       Jwj1j0C($                           
                      $$okkk*&Lxxxxd        h_IIIIM $                           
                      $Wkh8qxxxxxxx#        OIIXbIX *                           
                       $mxxxxxxxxxxq        aII[wI# z                           
                        cxxxxxxxxxxxI       uIII\j  -                           
                        Jxxxxxxxxxxxp      fhIII_h  >                           
                        kxxxxxxxxxxx0p    n"  -(                                
                        $xxxxxxxxxJh  >p8#phpCnnnCppI$    $$$                   
                        $xxxxxxuWcx  pf             p$ $}    n$                 
                        $xxxJ#dxxx0  n              n$8       f                 
                         xxxxxxxxx#  p              z$         $                
                         Jxxxxxxxx#  O              h"         h                
                         kxxxxxxxx#   "            "8          O                
                         Bxxxxxxxxm   p            pI          p                
                     $$$ $xxxxxxxxxI   h         "O}           8                
                    #kkk$$xxxxxxxxx8    "hn- --zO  $           $                
                   $kkkk%$xxxxxxxxxJ      -npnn-  fh           $                
                   $kkkkM$xxxxxxxxxxk            CxC          }                 
                    akkk$$xxxxxxxxxxxq>         Wxxz          $                 
                    $$$$ Bxxxxxxxxxxxxx8}    fhcxxxh         I                  
                         qxxxxxxxxxxxxxxxxJYxxxxxxxm         $                  
                         JxxxxxxxxxxxxxxxxxxxxxxxJd#(       h                   
                       $$xxxxxxxxxxxxxxxxxxxJW$$    $-     8                    
                      h" xxxxxxxxxxxxxxxxc@$          $pp$$                     
                     $   uxxxxxxxxxxxxx0$                                       
                     O   #xxxxxxxxxxxJ$                                         
                     >   >xxxxxxxxxu$                                           
                          Cxxxxxxuk$                                            
                           #xxxxx8$                                             
                            (ocJ$                                               
                     -          8                                               
                     O                                                          
                     $           $                                              
                      O          $                                              
                       $"       n                                               
                        $*I    p$                                               
                           $$$                                                  
                                                                                
 '''                                                                               
#解析数据
def analysis(res):
    ip_address=BeautifulSoup(res.text, "lxml").find_all('code')
    print(ip_address)
    


#------------------------------------主程序-----------------------------------------
if __name__ == '__main__':
    print('--------------spider start---------------')
    os.chdir(os.getcwd ())
    headers = get_headers()

    #是否使用代理（0不使用，1使用）
    proxies= is_or_not_proxy(0)


    #是否使用Cookie
    cookiess ={'Cookie':''}

    try:
        res=requests.get(url="http://ip.cn/", proxies=proxies,timeout=30,headers=headers,cookies=cookiess)
        
    except:
        print('使用代理获取网页失败')
    try:
        analysis(res)

    except:
        print('解析失败')
    print('--------------spider end---------------')
