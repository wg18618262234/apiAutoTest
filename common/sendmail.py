import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(username,password,sender,receiver,msg):
    smtp=smtplib.SMTP()
    smtp.connect('smtp.163.com,25')
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

def build_email():
    pass