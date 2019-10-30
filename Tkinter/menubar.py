import tkinter as tk

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小

lb = tk.Label(windows, bg='blue', width=10)
lb.pack()

def command1():
    pass

mb = tk.Menu(windows)  # 创建窗口上的menu，此时无内容
filemenu = tk.Menu(mb, tearoff=0)  # tearoff为0时表示不可分离,此filemenu可以理解为主选单
mb.add_cascade(label='file', menu=filemenu)  # 创建menu主选单，其中显示file
filemenu.add_command(label='command1', command=command1)


windows.mainloop()



