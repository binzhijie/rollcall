import pyperclip
from tkinter import messagebox

l=[]
print("请输入名字,例：\n小明\n小红\n小黄\n...\n\n按'x'退出。请输入:")
while True:
    a=input()
    if a=='x':
        break
    l.append(a)
pyperclip.copy(str(l))
print(l)
messagebox.showinfo("Tips:","已复制至剪贴板")