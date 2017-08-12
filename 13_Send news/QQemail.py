#---------------------------发邮件-------------------------------------------
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

def send_email(pwd_code,receiver_email,html):
    #qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    #sender_qq为发件人的qq号码
    sender_qq = '433289'
    #pwd为qq邮箱的授权码
    pwd = pwd_code
    #发件人的邮箱
    sender_qq_mail = '433289@qq.com'
    #收件人邮箱
    receiver = receiver_email
    #邮件的正文内容
    mail_content = html
    #newstxt
    #邮件标题
    mail_title = 'News (autosend by python)'

    #ssl登录
    smtp = SMTP_SSL(host_server)
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "html", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()
    print('已发送')
    #只需要更改host_server 、sender_qq、pwd、sender_qq_mail、receiver、mail_content、mail_title等数据，就可以实现简单的发送任务。
    #MIMEText函数中的第二个参数为“plain”时，发送的是text文本。如果为“html”，则能发送网页格式文本邮件。
