#!Python3
#浏览器自动填写账号和密码

import pyautogui,pyperclip,openpyxl,os,tkinter.messagebox 
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG )
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

r=''
rr=''
rrr=''
rrrr=''
#NO1,账号和密码获取
wb = openpyxl.load_workbook('password.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
def get_highest():
    for i in range(3,100):
        num='B'+str(i)
        if not sheet[num].value:
            num='B'+str(i-1)
            return(num)
            break
highest=get_highest()
lastnum=int(highest.strip('B'))
logging.debug(highest)
logging.debug(lastnum)
Alldata=[]
for n in range(3,lastnum+1):
    urlnum='C'+str(n)
    namenum='D'+str(n)
    passwordnum='E'+str(n)
    numbernum='F'+str(n)
    enternum='G'+str(n)
    Dict={'url':sheet[urlnum].value,'name':sheet[namenum].value,'password':sheet[passwordnum].value,'number':sheet[numbernum].value,'enter':sheet[enternum].value}
    logging.debug(Dict)
    Alldata.append(Dict)
submitbutton=sheet['H3'].value
submitbutton=submitbutton[1:-1]
submitbutton=tuple(submitbutton.split(','))
logging.debug(Alldata)

#NO.2 获取对应的字典数据

pyautogui.click(submitbutton)
pyautogui.keyDown('ctrl') 
pyautogui.keyDown('a') 
pyautogui.keyUp('a')
pyautogui.keyDown('c') 
pyautogui.keyUp('c') 
pyautogui.keyUp('ctrl')
weburl=pyperclip.paste()
e=0
for k in Alldata:
    if weburl in k.values():
        e=Alldata.index(k)
        break
    else:
        e=-1
logging.debug(e)
logging.debug(Alldata)
if e!=-1:  
    formdata=Alldata[e]
    logging.debug(formdata)
    logging.debug(type(formdata))
    url=formdata['url']        
    name=str(formdata['name'])
    password=formdata['password']
    number=formdata['number']
    enter=formdata['enter']
    logging.debug(type(name))
    logging.debug(type(password))


#No.3 填写数据
    logging.debug('enter data')   
    for e in range(int(number)):
        pyautogui.typewrite('\t')
    pyautogui.typewrite(name)
    pyautogui.typewrite('\t')
    pyautogui.typewrite(password)
    if enter==1:
        pyautogui.press('enter')
        pyautogui.press('enter')

#No.4 添加账号
else:
    top = tkinter.Tk()
    l = tkinter.Label(top,text="添加账号")
    l.pack()
    mb.showinfo("消息框","账号不存在，请添加")
    r= dl.askstring("SimpleDialog-Title","输入账号ID（抱歉，不支持中文）")
    rr = dl.askstring("SimpleDialog-Title","输入password")
    rrr = dl.askstring("SimpleDialog-Title","Tab次数")
    rrrr = dl.askstring("SimpleDialog-Title","不能直接回车请输入1")

#No.4 更新电子表格数据
    newnum=str(lastnum+1)
    sheet['B'+newnum]= str(int(newnum)-2)
    sheet['C'+newnum]= weburl    
    sheet['D'+newnum]= r
    sheet['E'+newnum]= rr
    sheet['F'+newnum]= rrr
    sheet['G'+newnum]= rrrr
    wb.save('password.xlsx')
    mb.showinfo("消息框","新账号已添加，关闭程序重新运行即可")
    top.mainloop() 
    
#No.5登录及结束程序
logging.debug('done')
