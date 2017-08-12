#!python3

from email.header import Header
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr, formatdate
def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_mail( from_email,passwd,to_emails,content):
    smtp_server = 'smtp.126.com' 
    subject = 'Autosend by python'
    # 指定subtype为alternative，同时支持html和plain格式
    msg = MIMEMultipart('alternative')
    
    #msg.attach(MIMEText(str(content), 'plain', 'utf-8'))       # 纯文本
    msg.attach(MIMEText(content, 'html', 'utf-8'))         # HTML



    # 未指定用户别名，则客户端会自动提取邮件地址中的名称作为邮件的用户别名
    msg['from'] = format_addr(from_email)
    msg['To'] = format_addr(to_emails)
    #msg['To'] = '%s' % ','.join([format_addr('<%s>' % to_email)for to_email in to_emails])

    msg['Subject'] = Header(str(subject), 'utf-8')
    msg['Date'] = formatdate()


    # 发送邮件
    try:
        # SMTP服务器设置(地址,端口):
        server = smtplib.SMTP_SSL(smtp_server, 465)
        # server.set_debuglevel(1)
        # 连接SMTP服务器(发件人地址, 客户端授权密码)
        server.login(from_email, passwd)

        # 发送邮件
        server.sendmail(from_email, to_emails, msg.as_string())

        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print(e)
        print('邮件发送失败')

    finally:
        # 退出SMTP服务器
        server.quit()

if __name__=='__main__':
    send_mail(from_email,passwd,to_emails,content = html)
