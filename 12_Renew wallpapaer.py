
#python3
#renew the computer wallpaper from bing.com

import os,requests,re
os.chdir (os.getcwd ())
import win32con
import win32api, win32gui
from PIL import Image
i=0 #数字0到7都可以
url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx='+str(i)+'&n=1&nc=1361089515117&FORM=HYLH1'
pic=re.compile(r'"url":"(.*?)","urlbase"')

res=requests.get(url)


picurl=re.findall(pic,res.text)
pic_url="http://cn.bing.com/"+picurl[0]

print('Find the url:{}......'.format(pic_url))


filename= pic_url.split('_')[-2]+'.'+pic_url.split('.')[-1]
print(filename)
def get_pic(url):
    picture=requests.get(url)
    print('Downloading '+filename+'......')
    imagepath=str(i)+filename
    with open(imagepath,'wb') as f:
        f.write(picture.content)
    return(imagepath)
pic=get_pic(pic_url)
print(pic)


##def setWallpaperFromBMP(imagepath):  
##    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
##    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
##    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
##    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)
##   
##    # convert jpg to bmp
##def setWallPaper(imagePath):
##    bmpImage = Image.open(imagePath)
##    newPath = imagePath.replace('.jpg', '.bmp')
##    bmpImage.save(newPath, "BMP")
##    setWallpaperFromBMP(newPath)
##
##setWallPaper(pic)
print('done')
