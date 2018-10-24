import smtplib
import base64
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import COMMASPACE


'''
Here to open smtp access for gmail
https://myaccount.google.com/lesssecureapps
'''
SENDER = 'xxx@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
USER_ACCOUNT = {'username':'xxx@gmail.com', 'password':'xxx'}
SUBJECT = "Test Test"


def send_mail(receiver, text, sender=SENDER, user_account=USER_ACCOUNT, subject=SUBJECT):
    msg_root = MIMEMultipart()  # 创建一个带附件的实例
    msg_root['Subject'] = subject  # 邮件主题
    msg_root['To'] = receiver  # 接收者
    msg_text = MIMEText(text, 'html', 'utf-8')  # 邮件正文
    msg_root.attach(msg_text)  # attach邮件正文内容
    try:
        smtp = smtplib.SMTP('smtp.gmail.com:587')
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user_account['username'], user_account['password'])
        smtp.sendmail(sender, receiver, msg_root.as_string())
        smtp.close()
        print('Email sent!')
    except:
        print('Something went wrong...')

if __name__=="__main__":
    receiver_list=['xxx@outlook.com','xxx@usc.edu']
    text=""
    for receiver in receiver_list:
        subject=""
        send_mail(receiver, text="你好",subject="Mentorship Pairing Result")