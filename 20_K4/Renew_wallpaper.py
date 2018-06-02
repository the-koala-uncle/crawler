#!python
#@author: the_koala_uncle
#@file:   renew_wallpapaer.py
#@time:   2017/8/14 11:59
#@desc:   renew_wallpapaer

import requests, os, time,re,configparser
os.chdir(os.getcwd())
from PIL import Image



tim=(str(time.time()*1000)[:13])
index='0'#数字0到7都可以

#url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx='+str(i)+'&n=1&nc=1361089515117&FORM=HYLH1'
url='http://cn.bing.com/HPImageArchive.aspx?format=js&idx=' + index + '&n=1&nc=' + tim + '&pid=hp'


def Download_pic(datapath):
    try:
        res=requests.get(url)
    except:
        print('网址错误')

        return
    data=res.json()
    targit_url='http://cn.bing.com'+ data['images'][0]['url']
    targit_name = data['images'][0]['copyright']
    print(targit_url)
    #print(targit_name)
    try:
        pic=requests.get(targit_url,timeout=30)
    except:
        print('图片网址网速不佳')

        return
    try:
        name = re.findall('[\u4e00-\u9fa5]*', targit_name)
        config = configparser.ConfigParser()
        config.read(datapath)

        paths = config.get('path','wallpaper')

        file = paths + name[0]+'_'+name[2] + targit_url[-4:]
        print('Found',file, sep=':')

        if os.path.isfile(file):
            print('图片已存在')
            os.startfile(file)

            return

        with open(file,'wb')as f:
            f.write(pic.content)
            print('下载完成')
    except:
        print('图片命名错误')

        return
    time.sleep(2)
    os.startfile(file)

##    im=Image.open(file)
##    im.show()
##    im.close()



# import win32con
# import win32api, win32gui
# from PIL import Image
# def setWallpaperFromBMP(imagepath):
#     k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
#     win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  # 2拉伸适应桌面,0桌面居中
#     win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
#     win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagepath, 1 + 2)
# # convert jpg to bmp
# def setWallPaper(imagePath):
#     bmpImage = Image.open(imagePath)
#     newPath = imagePath.replace('.jpg', '.bmp')
#     bmpImage.save(newPath, "BMP")
#     setWallpaperFromBMP(newPath)
# setWallPaper(pic)
