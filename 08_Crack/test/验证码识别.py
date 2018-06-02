from PIL import Image
from PIL import ImageGrab
import os,math
os.chdir(os.getcwd())

path="2.jpg"
def screenshot(x1,y1,x2,y2):
    im = ImageGrab.grab() 
    img_size = im.size
    region = im.crop((x1, y1, x2, y2))
    region.save("temp1.jpg")

##########################将验证码转化为灰度图，根据每一点的亮度剃掉噪点#############
def grayscale_clearNoise(path):
    im=Image.open(path)
    imgry=im.convert("L")#转化到灰度图
    imgry.save("temp1.jpg")
    threshold=100#140
    table=[]
    for i in range(256):
        if i <threshold:
            table.append(0)
        else:
            table.append(1)
            
    im2=imgry.point(table,'1')
    '''im.point(function) #,这个function接受一个参数，且对图片中的每一个点执行这个函数
        比如：out = im.point(lambda i : i*1.5)#对每个点进行50%的加强'''


    im2.save('temp2.jpg')
    return(im2)

##########################4邻域算法#############

def neighborhood_clearNoise(im2):
    image=im2.resize((110, 44))#放大尺寸    
    x,y=(image.size)
    #print(image.size)
    for i in range(x):
        for j in range(y):#while is 1 
            if int(image.getpixel((i,j)))==0:#0是黑色，1是白色

                try:

                    if image.getpixel((i+1,j-1))== 1 and image.getpixel((i+1,j+1))== 1 and image.getpixel((i-1,j+1))== 1 and image.getpixel((i-1,j-1))== 1:
                        image.putpixel((i,j),1)
                        #print(i,j)

                except:
                    pass
    image.save("temp3.jpg")
    return(image)


##########################切割##########################

def cut(im2):
      
    inletter = False
    foundletter=False
    start = 0
    end = 0

    letters = []

    for y in range(im2.size[0]): # slice across
        for x in range(im2.size[1]): # slice down
            pix = im2.getpixel((y,x))
            if pix != 1:
                inletter = True

        if foundletter == False and inletter == True:
            foundletter = True
            start = y

        if foundletter == True and inletter == False:
            foundletter = False
            end = y
            if int(end) -int(start)>4:
                letters.append((start,end))
            



        inletter=False
    print(letters)
    return(letters)
def ocr(letters,im2):
    class VectorCompare:
        def magnitude(self,concordance):
            total = 0
            for word,count in concordance.items():
                total += count ** 2
            return math.sqrt(total)

        def relation(self,concordance1, concordance2):
            relevance = 0
            topvalue = 0
            for word, count in concordance1.items():
                if word in concordance2:
                    topvalue += count * concordance2[word]
            return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))



    def buildvector(im):
        d1 = {}

        count = 0
        for i in im.getdata():
            d1[count] = i
            count += 1

        return d1

    v = VectorCompare()


    iconset = ['0','1','2','3','4','5','6','7','8','9','0']#,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


    imageset = []

    for letter in iconset:
        for img in os.listdir('./iconset/%s/'%(letter)):
            temp = []
            if img != "Thumbs.db" and img != ".DS_Store": # windows check...
                temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
            imageset.append({letter:temp})
    count = 0
    result=[]            
    for letter in letters:
        im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
        guess = []

        for image in imageset:
            for x,y in image.items():
                if len(y) != 0:
                    guess.append( ( v.relation(y[0],buildvector(im3)),x) )

        guess.sort(reverse=True)
        print("",guess[0])
        result.append(guess[0][1])
        
        count += 1
    return(result)
    
##########################
if __name__ == '__main__':
    print('---start---')
##    screenshot(788,671,846,694)#截图
    a=neighborhood_clearNoise(grayscale_clearNoise("temp1.jpg"))#降噪
    b=cut(a)#切割
    ocr(b,a)
    print('---end---')
