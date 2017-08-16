#!python
#@author: the_koala_uncle
#@file:   Control computer.py
#@time:   2017/8/13 13:32
#@desc:   Control computer

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import os, time, configparser, sys

date_list=[]
os.chdir(os.getcwd())

# ------------------------------------------------------------------------
try:
    config=configparser.ConfigParser()
    config.read('_config.ini')
    email = config.get('emailbox','user')
    password = config.get('emailbox','psw')
    pop3_server = config.get('emailbox','pop3')
except:
    print('缺乏有效账户！')
    input()
    sys.exit()
# ------------------------------------------------------------------------
#import pyautogui
##pyautogui.keyDown('win')
##pyautogui.keyDown('d')
##pyautogui.keyUp('win')
##pyautogui.keyUp('d')
# ------------------------------------------------------------------------
def run(code,i):
    if code:
        code =str(code)
        print('开始执行命令···{}···'.format(code))
        try:
            if code == '关机':
                os.system('shutdown -s -f -t 60')
                time.sleep(20)
                sys.exit()
            elif code[0] == '关':
                file= config.get('system',code)
                os.system(file)
                
            else:
                file= config.get('startfile',code)
                os.startfile(file)

        except Exception as e:
            print(e)
    else:
        print('主人，请指示······({})'.format(i))


# ------------------------------------------------------------------------


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


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    run_time= config.get('time','run')
    sleep= config.get('time','sleep')
    for i in range(int(run_time)):
        code = rerutn_code()
        run(code, i)
        time.sleep(int(sleep))
