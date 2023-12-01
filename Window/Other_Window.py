import time
from tkinter import *
import os

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

class Loading:
    def loading_window(self):
        self.window = Tk()
        self.window.overrideredirect(True)

        image_file = fr"img/Loading.jpg"
        photo = PhotoImage(file=image_file)

        self.label = Label(self.window, image=photo)
        self.label.pack()

        self.activity_text = Label(self.window,text='Loading...',bg='#060030',fg='white')
        self.activity_text.place(x=5,y=415)

        set_windows_x_y(self.window, 700, 445)

        self.window.mainloop()

    def set_text(self,text):
        self.activity_text.config(text=text)

    def quit_window(self):
        self.window.quit()

if __name__ == '__main__':
    window = Loading()
    window.loading_window()