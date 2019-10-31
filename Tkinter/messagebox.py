import tkinter as tk
import tkinter.messagebox  # 导入messagebox模组

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小


def hit_me():  # 弹窗函数
    # tk.messagebox.showinfo(title='Error', message='You get some problem╮(╯﹏╰）╭')  # 显示提示信息
    # tk.messagebox.showwarning(title='Error', message='You get some problem╮(╯﹏╰）╭')  # 显示警告信息，与上一个相似，图标不同
    tk.messagebox.showerror(title='Error', message='You get some problem╮(╯﹏╰）╭')

bt = tk.Button(windows, text='hit me',command=hit_me).pack()
windows.mainloop()

