# PYTHON3
# 图片转成字符画
from PIL import Image
import os

road=os.getcwd()    #获取当前工作目录
os.chdir(road)    #切换目录
WIDTH=80
HEIGHT=80

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

inn=input('放在同一目录下的图片名(如a.jpg),填写：')
im=Image.open(inn)

im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
txt = ""

for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((j,i)))
    txt += '\n'
print(txt)

with open('output.txt','w') as f:
    f.write(txt)



