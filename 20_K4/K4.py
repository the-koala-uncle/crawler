#!python3
#2017/8/18
#多功能程序包
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import os, time, configparser, sys, threading, hashlib,requests,json,pyperclip,psutil
#import pyautogui

# -------------------------------------------基本设置-------------------------------------------------------------------
os.chdir(os.getcwd())
filepath = 'E:\collection\_config.ini'
Allthread = []
task_list=[]
date_list=[]
##pyautogui.keyDown('win')
##pyautogui.keyDown('d')
##pyautogui.keyUp('win')
##pyautogui.keyUp('d'))

if not os.path.isfile(filepath):
    print('数据文件不存在，即将退出')
    time.sleep(5)
    sys.exit()

# -------------------------------------------读取数据-------------------------------------------------------------------
config = configparser.ConfigParser()
config.read(filepath)
email = config.get('emailbox','user')
password = config.get('emailbox','psw')
pop3_server = config.get('emailbox','pop3')
run_time = config.get('time', 'run')
sleep = config.get('time', 'sleep')
appid = config.get('fanyi_baidu','ID')
psw = config.get('fanyi_baidu','密钥')

# -------------------------------------------执行命令--------------------------------------------------------
def thread(code):
    if code:
        code = str(code)
        try:
            exec(code)
        except:
            print('开始执行命令···{}···'.format(code))
            try:
                try:
                    file = config.get('main', code).split(',')
                    exec(file[0])
                    print('---')
                    exec(file[1])
                    return
                except:
                    file = config.get('main', code)
                    exec(file)
                    return
            except:
                pass
            try:
                if code == '关机':
                    os.system('shutdown -s -f -t 60')
                    time.sleep(20)
                    sys.exit()
                elif code[0] == '关':
                    file = config.get('system', code)
                    os.system(file)

                else:
                    file = config.get('startfile', code)
                    os.startfile(file)

            except:
                temp_tran=translate(code)
                print('------------------')
                print('翻译结果为：')
                print(temp_tran)
                print('------------------')
# -------------------------------------------多进程--------------------------
def thread_more(de):
    if len(Allthread)!=0:
        for thr in Allthread:
            if thr.is_alive():
                pass
            else:
                thr.join()
                Allthread.remove(thr)
    t = threading.Thread(target=thread(de))
    t.daemon = True
    Allthread.append(t)
    t.start()
# -------------------------------------------关闭其他程序-----------------------
def kill(path):
    global task_list
    pidList = psutil.pids()

    for pid in pidList:

        pidDictionary = psutil.Process(pid).as_dict(attrs=['name']);
        for keys in pidDictionary.keys():
            w =str(pidDictionary['name'])
            try:
                config.get('task',w)               
            except:
                try:
                    psutil.Process(int(pid)).terminate()
                    task_list.append(w)
                except:
                    print(w+'没有被结束')

    print('以下进程已被终止：')                           
    for tem in task_list:
        print(tem)
    task_list=[]
    print('-------end-------')
# -------------------------------------------读取邮件-------------------------------------------------------------------
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def get_title(msg):
    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            if header == 'Subject':
                value = decode_str(value)
                return (value)

# 下载原始邮件
def rerutn_code():
    global date_list
    server = poplib.POP3(pop3_server)  # 命名
    server.set_debuglevel(0)  # 是否开启调试
    ##print(server.getwelcome().decode('utf-8'))#打印欢迎字样
    server.user(email)  # 添加账号
    server.pass_(password)  # 添加密码
    # 打印邮件数量和占用空间
    resp, mails, octets = server.list()
    ##print(mails)

    # 解析邮件
    index = len(mails)
    temp_list = []
    for i in range(5):# 取最新5件邮件
        resp, lines, octets = server.retr(index - i)  # 取最新一件邮件
        msg_content = b'\r\n'.join(lines).decode('utf-8')  # 粘结正文
        msg = Parser().parsestr(msg_content)
        temp_list.append(get_title(msg))
    server.quit()

    if date_list == []:
        date_list = temp_list
    if date_list==temp_list:
        return (False)
    else:
        date_list = temp_list
        return (date_list[0])
def email_control():
    for i in range(int(run_time)):
        
        temp_code = rerutn_code()
        if temp_code:
            print(temp_code)
        else:
            print('（{}）远程等待指示'.format(i+1))
        thread_more(temp_code)
        time.sleep(int(sleep))
def email_control1():
    for i in range(int(run_time)):
        time.sleep(1230)
        temp_code = rerutn_code()
        if temp_code:
            print(temp_code)
        else:
            print('（{}）20分钟远程等待指示'.format(i+1))
        thread_more(temp_code)
        

# -------------------------------------------翻译---------------------

def md5(word):
    word = word.encode("utf-8")  
    m= hashlib.md5()  
    m.update(word)  
    return m.hexdigest()
def is_alphabet(uchar):
    if (uchar>= u'\u0041'and uchar<=u'\u005a')or(uchar >= u'\u0061'and uchar<=u'\u007a'):
        return(True)
    else:
        return(False)
def translate(q):
    if is_alphabet(q):
        fromm= 'en'
        to='zh'
    else:
        fromm= 'zh'
        to='en'
    salt='143620287'

    sign=md5(appid+q+salt+psw)
    
    url='http://api.fanyi.baidu.com/api/trans/vip/translate?q='+q+'&from='+fromm+'&to='+to+'&appid='+appid+'&salt='+salt +'&sign='+sign
    try:
        res=requests.get(url)

        json_dict=json.loads(res.text)
        try:
            return(json_dict["trans_result"][0]["dst"])
        except:
            return(res.text)

    except:
        return('无法翻译')
        

# -------------------------------------------主程序--------------------------------
t = threading.Thread(target=email_control1)
t.daemon = True
Allthread.append(t)
t.start()

while 1:


    index = input('请指示！')
    if index=='':
        index= pyperclip.paste()
    if index=='running':
        print('子进程正在运行数量为：'+str(len(Allthread)))
        print(Allthread)
    elif index[0:2]=='百度':
        os.startfile('https://www.baidu.com/s?wd='+index[2:])
    elif index[0:5]=='baidu':
        os.startfile('https://www.baidu.com/s?wd='+index[5:])
    elif index=='start':
        os.startfile(filepath[:-12])
    elif index=='con':
        t = threading.Thread(target=email_control)
        t.daemon = True
        Allthread.append(t)
        t.start()
    elif index=='kill':
        kill(filepath)

    elif index=='end':
        break
    else:
        try:
            thread_more(index)
        except Exception as e:
            print(e)
            print('未能启动进程')

