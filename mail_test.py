import smtplib
from email.mime.text import MIMEText
from email.header import Header
from tkinter import messagebox

msg_from = 'bzjvip@sohu.com'
password = '36GWRSJY9ZD10E'

def go_mail(msg_to, yanzhengma):
    # ------------------------login------------------------#
    s = smtplib.SMTP('smtp.sohu.com', '25')
    s.login(msg_from, password)
    # -----------------------------------------------------#
    subject = 'RollCall验证码'
    msg = MIMEText(f'欢迎使用RollCall！\n你的验证码是：{yanzhengma}')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = msg_from
    try:
        s.sendmail(msg_from, msg_to, msg.as_string())
        print('成功')
        messagebox.showinfo('Tips:','发送成功!')
        try:
            ok = MIMEText(f'有一名用户接收了一个验证码\n邮箱：{msg_to}\n验证码：{yanzhengma}')
            ok['Subject'] = Header('有人接收了一个验证码', 'utf-8')
            ok['From'] = msg_from
            s.sendmail(msg_from, 'bzjvip@126.com', ok.as_string())
        except:
            print('二环节发送失败')
    except:
        print('失败')
        messagebox.showerror('Tips:','发送失败！')
    finally:
        s.quit()

# Email('bzjvip@126.com', '123456')