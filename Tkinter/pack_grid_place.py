import tkinter as tk
import tkinter.messagebox  # 导入messagebox模组

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小

# pack中side的各种设置
# tk.Label(windows, text='label', bg='black').pack(side='top')
# tk.Label(windows, text='label', bg='black').pack(side='bottom')
# tk.Label(windows, text='label', bg='black').pack(side='left')
# tk.Label(windows, text='label', bg='black').pack(side='right')

# grid网格式放置
for i in range(4):
    for j in range(3):  # 四行三列
        tk.Label(windows, text=1).grid(row=i, column=j)  # 注意调用网格时不要同时使用pack


windows.mainloop()

