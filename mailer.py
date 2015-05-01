import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

class Emailer:
    def __init__(self,addr='',pw='',receiver='',subject=None):
        self.addr = addr
        self.pw = pw
        self.msg = MIMEMultipart('alternative')
        self.receiver = [receiver]
        if subject:
            self.msg['Subject'] = subject
        else:
            self.msg['Subject'] = "Generic Subject"
        self.msg["From"]=self.addr
        self.msg["To"] = ','.join(self.receiver)
        
    def add_message(self,text):
        if type(text) == type(' '):
            tmp = MIMEText(text,'plain')
            self.msg.attach(tmp)
    def send(self):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.addr, self.pw)
        s.sendmail(self.addr, self.receiver, self.msg.as_string()) 
        s.close()

if __name__ == '__main__':
    crds =json.load(open("creds.json","r"))
    mailer = Emailer(addr=crds["addr"],pw=crds["pw"])
    
