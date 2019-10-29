import tkinter as tk

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小


cv = tk.Canvas(windows, bg='blue', width=300, height=500)  # 画布，用于放置图片图形等
cv.pack()


def fun():
    pass


bt = tk.Button(windows, text='move', command=fun)
bt.pack()

# 在画布上放置图片
image_file = tk.PhotoImage(file='.\\image\\photo_test.gif')  # 注意文件路径的表达形式
image = cv.create_image(0, 0, anchor='nw', image=image_file)  # anchor代表锚定点，（0.0）为坐标.此处代表此点为center或nw






windows.mainloop()  # 主循环
