import tkinter as tk
import tkinter.messagebox  # 导入messagebox模组

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小


def hit_me():  # 弹窗函数
    # tk.messagebox.showinfo(title='Error', message='You get some problem╮(╯﹏╰）╭')  # 显示提示信息
    # tk.messagebox.showwarning(title='Error', message='You get some problem╮(╯﹏╰）╭')  # 显示警告信息，与上一个相似，图标不同
    # tk.messagebox.showerror(title='Error', message='You get some problem╮(╯﹏╰）╭')
    ans = tk.messagebox.askquestion(title='Please answer', message='Do you want to do something?')  # 此函数返回'yes'以及'no'
    # 根据用户结果作出处理
    if ans == 'yes':
        print('yes')
    else:
        print('no')

    anstf = tk.messagebox.askyesno(title='Please answer', message='Do you want to do something?')  # 此函数返回'True'以及'False'
    tk.messagebox.askokcancel(title='Please answer', message='Do you want to do something?')  # 返回True及False
    tk.messagebox.asktrycancel(title='Please answer', message='Do you want to do something?')  # 返回True及False
    # 根据用户结果作出处理
    if anstf == True:  # 注意此处True非字符型
        print('True')
    else:
        print('False')



bt = tk.Button(windows, text='hit me',command=hit_me).pack()
windows.mainloop()


