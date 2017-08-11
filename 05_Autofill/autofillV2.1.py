#!Python3
#浏览器自动填写账号和密码

import pyautogui,pyperclip,os,tkinter.messagebox,encrypted
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

#NO.1 监控鼠标
#NO.2 账号和密码获取
x, y = pyautogui.position() 
f = open('6f9rg46fgf5rfeg75rg5gt9er.txt') 
line=f.readlines()
f.close()
num=len(line)
isin=False
for n in line:
    dictt=n.split(',')
    if dictt[0]=='0':
        pyautogui.click(tuple(eval(','.join([dictt[1],dictt[2]]))))
        pyautogui.keyDown('ctrl') 
        pyautogui.keyDown('a') 
        pyautogui.keyUp('a')
        pyautogui.keyDown('c')
        pyautogui.keyUp('c') 
        pyautogui.keyUp('ctrl')
        weburl=pyperclip.paste()
        if not weburl.startswith('http'):
            input()
    else:
        a=dictt[1]
        if weburl==a:
            isin=True

#No.3 填写数据
            s=encrypted.decryption(dictt[2])
            ss=encrypted.decryption(dictt[3][:-1])
            pyautogui.click(tuple(eval('%sstr(x).rjust(4), str(y).rjust(4)%s'%('(',')'))))
            pyautogui.typewrite(s)
            pyautogui.typewrite('\t')
            pyautogui.typewrite(ss)


#No.4 添加账号
if not isin:       
    top = tkinter.Tk()
    l = tkinter.Label(top,text="添加账号")
    l.pack()
    mb.showinfo("消息框","账号不存在，请添加")
    r= dl.askstring("SimpleDialog-Title","输入账号ID（抱歉，不支持中文）")
    rr = dl.askstring("SimpleDialog-Title","输入password")

#No.4 更新数据
    f = open('6f9rg46fgf5rfeg75rg5gt9er.txt','a')
    r=encrypted.encryption(r)
    rr=encrypted.encryption(rr)
    f.write("%s,%s,%s,%s"%(num,weburl,r,rr))
    f.write("\r\n")
    f.close()
    mb.showinfo("消息框","新账号已添加，关闭程序重新运行即可")
    top.mainloop()
