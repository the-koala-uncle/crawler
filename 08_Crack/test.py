from PIL import Image
import hashlib
import time
import os
os.chdir(os.getcwd())
im = Image.open("1397.gif")
###############测试一#################

im.convert("P")
his = im.histogram()
values = {}

for i in range(256):

    values[i] = his[i]

for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:

    print(j,k)
##############测试二##################
##im = Image.open("captcha1.gif")
##im.convert("P")
##im2 = Image.new("P",im.size,255)
##
##
##for x in range(im.size[1]):
##    for y in range(im.size[0]):
##        pix = im.getpixel((y,x))
##        if pix == 255 or pix == 197 or pix == 232: # 我们得到了图片中最多的10种颜色，其中 220 与 227 才是我们需要的红色和灰色，可以通过这一讯息构造一种黑白二值图片。
##
##            im2.putpixel((y,x),0)
##
##im2.show()

###############测试三#################


##im.convert("P")
##im2 = Image.new("P",im.size,255)
##
##
##for x in range(im.size[1]):
##    for y in range(im.size[0]):
##        pix = im.getpixel((y,x))
##        if pix == 224 or pix == 213 : # 我们得到了图片中最多的10种颜色，其中 220 与 227 才是我们需要的红色和灰色，可以通过这一讯息构造一种黑白二值图片。
##
##            im2.putpixel((y,x),0)
##im2.show()
##inletter = False
##foundletter=False
##start = 0
##end = 0
##
##letters = []
##
##for y in range(im2.size[0]): 
##    for x in range(im2.size[1]):
##        pix = im2.getpixel((y,x))
##        if pix != 255:
##            inletter = True
##    if foundletter == False and inletter == True:
##        foundletter = True
##        start = y
##
##    if foundletter == True and inletter == False:
##        foundletter = False
##        end = y
##        letters.append((start,end))
##
##    inletter=False
####print(letters)
##
##count = 0
##for letter in letters:
##    m = hashlib.md5()
##    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
##    m.update(str(count + time.time()).encode("utf-8"))
##    im3.save("./%s.gif"%(m.hexdigest()))
##    count += 1

###############测试四#################

##用 Python 类实现向量空间：
##
##import math
##
##class VectorCompare:
##    #计算矢量大小
##    def magnitude(self,concordance):
##        total = 0
##        for word,count in concordance.iteritems():
##            total += count ** 2
##        return math.sqrt(total)
##
##    #计算矢量之间的 cos 值
##    def relation(self,concordance1, concordance2):
##        relevance = 0
##        topvalue = 0
##        for word, count in concordance1.iteritems():
##            if concordance2.has_key(word):
##                topvalue += count * concordance2[word]
##        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))
##
##来源: 实验楼
##链接: https://www.shiyanlou.com/courses/364
##本课程内容，由作者授权实验楼发布，未经允许，禁止转载、下载及非法传播


