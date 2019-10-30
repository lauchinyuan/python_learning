import tkinter as tk

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小

lb = tk.Label(windows, bg='blue', width=10)
lb.pack()
counter = 0


def command1():
    global counter
    counter += 1
    lb.config(text='This is the '+str(counter)+' th')


def command2():
    global counter
    counter -= 1
    lb.config(text='This is the '+str(counter)+' th')


mb = tk.Menu(windows)  # 创建窗口上的menu，此时无内容
filemenu = tk.Menu(mb, tearoff=0)  # tearoff为0时表示不可分离,此filemenu可以理解为主选单
mb.add_cascade(label='file', menu=filemenu)  # 创建menu主选单，其中显示file
filemenu.add_command(label='command1', command=command1)  # 增加子菜单
filemenu.add_command(label='command2', command=command2)
filemenu.add_separator()  # 增加分隔线，用于界面美化
filemenu.add_command(label='exit', command=windows.quit())  # windows.quit用于退出

sub = tk.Menu(filemenu)  # 在filemenu下再创建一个sub
filemenu.add_cascade(label='more', menu=sub, underline=0)  # 显示该菜单
sub.add_command(label='command3', command=command1)
windows.config(menu=mb)  # 最后放置菜单

windows.mainloop()



