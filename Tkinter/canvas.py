import tkinter as tk

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小


cv = tk.Canvas(windows, bg='blue', width=150, height=100)  # 画布，用于放置图片图形等
cv.pack()

# 在画布上放置图片
image_file = tk.PhotoImage(file='photo.jpg')


def fun():
    pass
#  git

windows.mainloop()  # 主循环
