import tkinter as tk

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小


cv = tk.Canvas(windows, bg='blue', width=150, height=100)  # 画布，用于放置图片图形等
cv.pack()

# 在画布上放置图片
image_file = tk.PhotoImage(file='D:\\github\\python_learning\\Tkinter\\image\\photo_test.gif')  # 注意文件路径的表达形式


def fun():
    pass

windows.mainloop()  # 主循环
