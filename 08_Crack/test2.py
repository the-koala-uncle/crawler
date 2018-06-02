from PIL import Image
import hashlib
import time
import os
os.chdir(os.getcwd())
im = Image.open("5262.gif")
###############测试一#################

im.convert("P")
his = im.histogram()
values = {}

for i in range(256):

    values[i] = his[i]
color=[]
for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:

    print(j,k)
    if int(k)>7:
        color.append(int(j))
        

im2 = Image.new("P",im.size,255)


for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix in color and pix !=0: # 我们得到了图片中最多的10种颜色，其中 220 与 227 才是我们需要的红色和灰色，可以通过这一讯息构造一种黑白二值图片。

            im2.putpixel((y,x),0)
im2.show()
inletter = False
foundletter=False
start = 0
end = 0

letters = []

for y in range(im2.size[0]): 
    for x in range(im2.size[1]):
        pix = im2.getpixel((y,x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))

    inletter=False
##print(letters)

count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
    m.update(str(count + time.time()).encode("utf-8"))
    im3.save("./%s.gif"%(m.hexdigest()))
    count += 1

