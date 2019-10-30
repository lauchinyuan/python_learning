import tkinter as tk

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小


cv = tk.Canvas(windows, bg='black', width=300, height=500)  # 画布，用于放置图片图形等
cv.pack()


def fun():
    cv.move(rect, 0, 3)  # 表示每次调用函数时画布上的rect X轴移动0，Y轴移动3


bt = tk.Button(windows, text='move', command=fun)
bt.pack()

# 在画布上放置图片
image_file = tk.PhotoImage(file='.\\image\\photo_test.gif')  # 注意文件路径的表达形式
image = cv.create_image(0, 0, anchor='nw', image=image_file)  # anchor代表锚定点，（0.0）为坐标.此处代表此点为center或nw

# 在画布上绘制直线
x0, y0, x1, y1 = 0, 0, 40, 40  # 注意多项赋值的方法
line = cv.create_line(x0, y0, x1, y1, fill='red')  # fill代表填充颜色

# 在画布上绘制圆形
oval = cv.create_oval(x0, y0, x1, y1, fill='red')

# 在画布上绘制扇形
arc = cv.create_arc(100, 100, 150, 150, start=0, extent=180)  # 表示从零度收到180度

# 在画布上绘制矩形
rect = cv.create_rectangle(150, 150, 200, 200, fill='blue')



windows.mainloop()  # 主循环
