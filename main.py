#lighter 为细体，normal 为正常粗细，bold 为粗体，bolder 为特粗体
import Window.Other_Window

this_verion = '3.2'

def open_Web(url):
    webbrowser.open(url)

import tkinter
from tkinter import *
import random
from tkinter import messagebox
import time
import webbrowser
import mail_test
import import_name
from say import say
import Jilu
import os
import EasyMail
from configparser import ConfigParser
import Get_File
import Detection

def set_windows_x_y(window, window_width, window_height):
    # 设置窗口的宽度和高度
    window_width = window_width
    window_height = window_height

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 计算窗口的左上角位置，使其居中显示
    x_position = (screen_width - window_width) / 2
    y_position = (screen_height - window_height) / 2
    # 设置窗口的位置和大小
    window.wm_geometry(f"{str(window_width)}x{str(window_height)}+{str(int(x_position))}+{str(int(y_position))}")


if Detection.is_network_connected():
    web = True
    cache = Get_File.IniFileCache('https://binzhijie.github.io/rollcall_web_config/web_config.ini','web_config.ini')
    cache.save_to_cache()

    # 读取ini文件
    web_config = ConfigParser()
    web_config.read('web_config.ini',encoding='gbk')

    if web_config['options']['can_use'] == 'True':
        if web_config['options']['if_gonggao_show'] == 'True':
            messagebox.showinfo(web_config['text']['title'], web_config['text']['text'])
    else:
        messagebox.showinfo(web_config['text']['not_can_use_title'], web_config['text']['not_can_use_text'])
        os._exit(0)

else:
    web = False
    web_config = ConfigParser()
    web_config.read('web_config.ini')

    if web_config['options']['can_use'] == 'True':
        if web_config['options']['if_gonggao_show'] == 'True':
            messagebox.showinfo(web_config['text']['title'], web_config['text']['text'])
    else:
        messagebox.showinfo(web_config['text']['not_can_use_title'], web_config['text']['not_can_use_text'])
        os._exit(0)

    messagebox.showinfo('Tips:','当前为离线模式，建议联网使用')



def Check_for_updates(option):
    global web_config, cache
    if option == 1:
        del web_config,cache

        cache = Get_File.IniFileCache('https://binzhijie.github.io/rollcall_web_config/web_config.ini', 'web_config.ini')
        cache.save_to_cache()

        web_config = ConfigParser()
        web_config.read('web_config.ini', encoding='gbk')

    version = web_config['date']['version']
    if version > this_verion:
        ask = messagebox.askyesno('发现新版本',f'检测到软件有更新！\n最新版本：v{version}\n当前版本：v{this_verion}\n\n是否立即更新？')
        if ask == True:
            open_Web("https://www.123pan.com/s/K9i0Vv-JiSgH.html")
        return True
    elif version == this_verion:
        messagebox.showinfo('检查更新',f'当前已是最新版本！\n\n当前版本：v{this_verion}')
        return False


if web:
    version = web_config['date']['version']
    if version > this_verion:
        Check_for_updates(0)


#-------------------key--------------------------#

if_key = False

key = eval(web_config['date']['key'])

test_num = eval(web_config['date']['test_num'])

#-------------------------------------------------#

random_name_speed = ConfigParser()
random_name_speed.read('config.ini',encoding='gbk')
random_name_speed = int(random_name_speed['random_name']['speed'])
config = ConfigParser()
config.read('config.ini',encoding='gbk')

try:
    if_jihuo = open("data_file.txt", 'r', encoding='ansi')
    if_key = True
except:
    input_window = Tk()
    set_windows_x_y(input_window,250,200)
    input_window.iconbitmap('ico.ico')
    input_window.title('激活软件')

    def get_text(self):
        if self.get() in key:
            if input_test.get() in test_num:
                print(True)
                if_key = True
                open("data_file.txt", 'a+')
                user_mail = input_to.get()
                messagebox.showinfo('Tips:','激活成功！')
                input_window.destroy()
                print('正在发送欢迎语...')
                html = f"""<!DOCTYPE html>
                <html lang="en" xmlns="http://www.w3.org/1999/html">
                <head>
                    <meta charset="UTF-8">
                    <title>欢迎使用RollCall点名器</title>
                </head>
                <body>
                    <h1>欢迎使用RollCall点名器</h1>
                    <b>尊敬的邮箱账户“{str(user_mail)}”，你好！<br></b>
                    <b>感谢使用“RollCall点名器！”<br></b>
                    <b><br>帮助文档:<br></b>
                    <a href="https://www.cnblogs.com/bzjvip/articles/17737963.html">帮助文档</a>
                    <b><br>官网：<br></b>
                    <a href="https://binzhijie.github.io">官网</a>
                </body>
                </html>"""

                m = EasyMail.Mail_Server('smtp.sohu.com', 'bzjvip@sohu.com', '36GWRSJY9ZD10E')
                m.go_mail_html(user_mail, '欢迎使用RollCall点名器', html)
                print('ok')
                input_window.quit()
                return True
            else:
                print(False)
                messagebox.showerror('Tips:', '验证码错误！')
                return False
        else:
            print(False)
            messagebox.showerror('Tips:','激活码错误！')
            return False

    def make_test_num():
        global test_num, input_to
        test_num = ''
        for i in range(6):
            test_num+=str(random.randint(0,9))
        print(test_num)
        print(input_to.get())
        mail_test.go_mail(str(input_to.get()),test_num)

    label_key = Label(input_window, text='请输入激活码、邮箱、验证码（分别输入）:')
    label_key.place(x=5, y=10)

    input_key = Entry(input_window,show='')
    input_key.place(x=20, y=35)

    ok_key = Button(input_window, text='确定', command=lambda: get_text(input_key))
    ok_key.place(x=130, y=130)

    input_to = Entry(input_window, show='')
    input_to.place(x=20, y=65)

    input_test = Entry(input_window, show='')
    input_test.place(x=20, y=95)

    ok_test = Button(input_window, text='获得验证码', command=lambda: make_test_num())
    ok_test.place(x=20, y=130)

    fangwengguanwang = Button(input_window, text='获得激活码', command=lambda:open_Web('https://www.cnblogs.com/bzjvip/articles/17736276.html'))
    fangwengguanwang.place(x=170, y=35)


    input_window.mainloop()

if if_key == True:
    # 读取名字文件
    try:
        names_file = open("names_list.txt", 'r', encoding='ansi')
        names = eval(names_file.readline())
        all_names = len(names)
    except:
        open("names_list.txt", 'a+')
        names_list = open("names_list.txt", 'r', encoding='ansi')
        names = []
        all_names = len(names)
        messagebox.showinfo('Tips:','第一次使用记得添加名字哦！\nRemember to add a name when using it for the first time!')
    # names=eval(names_file.readline())

    window = tkinter.Tk()
    set_windows_x_y(window,500,300)
    window.resizable(0,0)
    window.title('RollCall_点名器')
    window.iconbitmap('ico.ico')
    # window.protocol("WM_DELETE_WINDOW", lambda:exit_window())

    time_now = time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())
    jilu = Jilu.jilu_start(f'{time_now}.txt')

#----------------------开始点名---------------------#
    def start_read_name():
        global name_Label, names, remaining_people,all_names
        if len(names) == 0:
            messagebox.showinfo('Tips:','所有人已经抽完了哦！点’重置‘以重新开始')
        else:
            random.shuffle(names)
            if var2.get():
                name_index = random.randint(0, len(names) - 1)
                name_temp = names[name_index]
                name_Label.configure(text=name_temp)

            else:
                # 随机显示名字
                s = 0
                for i in range(random_name_speed):
                    if s >= len(names):
                        s=0
                    else:
                        name_Label.configure(text=names[s])
                        s+=1
                        window.update()
                        # print(s)
                        time.sleep(0.01)
                name_index = random.randint(0, len(names)-1)
                name_temp = names[name_index]
                name_Label.configure(text=name_temp)
                # print(name_index)
                jilu.append_name(name_temp)
            window.update()

            speak_temp = str(name_temp)

            if var.get():
                restored()
            else:
                names.remove(name_temp)
            remaining_people.configure(text=f'剩下的人数:{len(names)}/{all_names}')
            print(len(names))
            print(names)
            print(name_temp)
            window.update()

            # --------------------------朗读文本---------------------#
            if speak_var.get():
                say(speak_temp+str(config['date']['speak_text']))
            # -----------------------------------------------------#
            window.update()

    def exit_window():
        cache.clear_cache()
        del cache
        window.quit()

    def restored():
        global names_file, names, name_Label,all_names
        names_file = open("names_list.txt", 'r', encoding='ansi')
        names = eval(names_file.readline())
        all_names = len(names)
        random.shuffle(names)
        remaining_people.configure(text=f'剩下的人数:{len(names)}/{all_names}')

    def about():
        messagebox.showinfo('About','这是一个面向部分群体的点名器，可以完美的解决主动点名的不公平性\n\n制作人：宾志杰')

    def help_no_online():
        messagebox.showinfo('使用说明','点击导入，\n点击后进入导入界面，\n在界面中输入需要导入的名字，\n点击“导入”，关闭窗口，即可正常使用。\n\n建议使用在线帮助文档')

    def top_windows():
        if top_window_var.get():
            window.wm_attributes('-topmost','true')
        else:
            window.wm_attributes('-topmost', 'false')
        print(top_window_var.get())
        window.update()

    name_Label = Label(window,
                       text='未开始',
                       font=('宋体',60,'bold')
                       )
    name_Label.place(x=100,y=10)

    start = Button(window,
                   text='开始点名',
                   font=('黑体',25),
                   width=11,
                   height=2,
                   command=lambda:start_read_name()
                   )
    start.place(x=100,y=120)

    restore = Button(window,
                     text='重置',
                     font=('黑体',15),
                     command=lambda:restored()
                     )
    restore.place(x=400,y=230)

    remaining_people = Label(window,
                             text=f'剩下的人数:{len(names)}/{all_names}',
                             font=('黑体',10)
                             )
    remaining_people.place(x=300,y=120)

    var = BooleanVar()
    var.set(False)
    chongfu = Checkbutton(window, text="重复模式", font=('黑体',10), variable=var, command=lambda:window.update())
    chongfu.place(x=300,y=140)

    var2 = BooleanVar()
    var2.set(False)
    kuaisu = Checkbutton(window, text="快速模式", font=('黑体',10), variable=var2, command=lambda:window.update())
    kuaisu.place(x=300,y=160)

    coastal = Label(window,text='Coastal Studio',font=('Arial',15,'normal'))
    coastal.place(x=5,y=250)

    speak_var = BooleanVar()
    speak_var.set(False)
    speak_button = Checkbutton(window, text='朗读结果', font=('黑体',10), variable=speak_var, command=lambda:window.update())
    speak_button.place(x=300,y=180)

    top_window_var = BooleanVar()
    top_window_var.set(False)
    top_window = Checkbutton(window,text='置顶窗口',font=('黑体',10),variable=top_window_var,command=lambda:top_windows())
    top_window.place(x=300,y=200)

    #-----------------标记--------------------------#
    biaoji = Button(window,text='标记',font=('黑体',10))
    # biaoji.place(x=416,y=205)
    #----------------------------------------------#

    #---------------Menu----------------#
    menu = Menu(window)

    tounch_menu = Menu(menu,tearoff=False)
    tounch_menu.add_command(label='导入',command=lambda:import_name.import_window())
    tounch_menu.add_command(label='记录',command=lambda:os.system('start .\\jilu'))
    tounch_menu.add_separator()
    tounch_menu.add_command(label='退出', command=window.quit)
    menu.add_cascade(label='操作',menu=tounch_menu)

    help_menu = Menu(menu,tearoff=False)
    help_menu.add_command(label='使用说明',command=lambda:open_Web('https://www.cnblogs.com/bzjvip/articles/17737963.html'))
    help_menu.add_command(label='使用说明(离线)',command=lambda:help_no_online())
    menu.add_cascade(label='帮助', menu=help_menu)

    about_menu = Menu(menu,tearoff=False)
    about_menu.add_command(label='Blogs',command=lambda:open_Web('www.cnblogs.com/bzjvip'))
    about_menu.add_separator()
    about_menu.add_command(label='检查更新',command=lambda:Check_for_updates(1))
    about_menu.add_command(label='关于',command=about)
    menu.add_cascade(label='关于',menu=about_menu)

    window.config(menu=menu)

    window.mainloop()