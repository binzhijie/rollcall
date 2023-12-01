from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import ansi

config = ConfigParser()
config.read('config.ini',encoding='gbk')

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


def get_name(self,window):
    if eval(config['options']['NameChange']):
        global wi
        names = self.get('0.0','end')
        print(names)
        names = names.split('\n')
        while '' in names:
            names.remove('')
        print(names)

        with open('names_list.txt','w',encoding='ansi') as f:
            f.write(str(names))
            f.close()
        messagebox.showinfo('Tips:','导入成功')
        window.destroy()
    else:
        messagebox.showerror('Error', '管理员锁定，无法更改')
        window.destroy()

def import_window():
    wi = Tk()
    set_windows_x_y(wi,450,300)
    wi.title('导入名字')
    wi.iconbitmap('ico.ico')

    name_input = Text(wi, width=55, height=18)
    name_input_scroll = Scrollbar(wi,borderwidth=280,elementborderwidth=50,width=20)

    name_input_scroll.pack(side=RIGHT,fill=Y)
    name_input.place(x=15, y=15)

    name_input_scroll.config(command=name_input.yview)
    name_input.config(yscrollcommand=name_input_scroll.set,width=55, height=18)

    get_name_button = Button(wi, text='导入',width=54,height=1,command=lambda:get_name(name_input,wi))
    get_name_button.place(x=15,y=260)

    try:
        names_list = open("names_list.txt", 'r', encoding='ansi')
        names = eval(names_list.readline())
        for i in names:
            name_input.insert('insert', i+'\n')
    except:
        pass

    wi.mainloop()
