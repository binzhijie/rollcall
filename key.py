from tkinter import *

key = 'bzjvip126'

input_window = Tk()
input_window.geometry('250x100')
input_window.iconbitmap('ico.ico')
input_window.title('激活码')

def get_text(self):
    if self.get() == key:
        print(True)
        return True
    else:
        print(False)
        return False

label_key = Label(input_window,text='请输入激活码:')
label_key.place(x=20,y=10)

input_key = Entry(input_window)
input_key.place(x=20,y=35)

ok_key = Button(input_window,text='确定',command=lambda:get_text(input_key))
ok_key.place(x=180,y=30)

def get_key():
    input_window.mainloop()