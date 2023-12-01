import smtplib
from email.mime.text import MIMEText

class Mail_Server:
    def __init__(self,host,user,passwd):
        self.host = host
        self.user = user
        self.passwd = passwd

        self.server = smtplib.SMTP_SSL(self.host, 465)
        self.server.login(self.user, self.passwd)

    def go_mail(self,to,title,text):
        self.msg = MIMEText(text,'plain', 'utf-8')
        self.msg['From'] = self.user
        self.msg['To'] = to
        self.msg['Subject'] = title

        try:
            self.server.sendmail(self.user,to,self.msg.as_string())
        except:
            print('---------------------发送失败------------------------')
            return False
        else:
            return True

    def go_mail_html(self,to,title,html_file):
        self.msg = MIMEText(html_file,'html', 'utf-8')
        self.msg['From'] = self.user
        self.msg['To'] = to
        self.msg['Subject'] = title

        try:
            self.server.sendmail(self.user,to,self.msg.as_string())
        except:
            print('---------------------发送失败------------------------')
            return False
        else:
            return True

    def quit(self):
        self.server.quit()