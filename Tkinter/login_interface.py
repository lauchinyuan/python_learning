# tkinter的综合应用，设计登录窗口
import tkinter as tk
import pickle
import tkinter.messagebox
windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小

#  页面logo
cav = tk.Canvas(windows, bg='white', width=280, height=180)  # 放置logo图片
photo_file = tk.PhotoImage(file='.\\image\\github logo.png')
cav.create_image(0, 0, anchor='nw', image=photo_file)
cav.pack(side='top')

#  用户提示信息
tk.Label(windows, text='User name:').place(x=600, y=200)
tk.Label(windows, text='Password:').place(x=600, y=220)

#  输入框
usr_name = tk.StringVar()  # 定义字符变量
usr_password = tk.StringVar()

tk.Entry(windows, textvariable=usr_name).place(x=680, y=200)
tk.Entry(windows, textvariable=usr_password, show='*').place(x=680, y=220)


#  按键 login and sign up及相关功能
def usr_login():
    #  获得输入信息
    user_name = usr_name.get()
    user_password = usr_password.get()
    try:  # 尝试打开用户信息文件
        with open('.\\file\\userinfo.pickle', 'rb') as file:
            user_info = pickle.load(file)
    except FileNotFoundError:  # 如果文件不存在
        tk.messagebox.showerror(title='Error', message='file not found')

    if user_name in user_info:  # 如果用户名存在
        if user_password == user_info[user_name]:  # 密码正确
            tk.messagebox.showinfo(title='Welcome', message='hello '+str(user_name))

        else:  # 如果用户输入密码不对
            tk.messagebox.showerror(title='Error', message='Your password is wrong! Please retry')
    else:  # 如果用户名不存在
        tk.messagebox.showerror(title='Error', message='User not found')


def usr_signup():
    def signup_ok():  # 确认注册
        # 获取用户输入值
        usname = texv1.get()
        pas = texv2.get()
        com_pas = texv3.get()
        try:  # 尝试开启文件，调用文件中的字典至本地
            with open('.\\file\\userinfo.pickle', 'rb') as file1:
                us_info = pickle.load(file1)
        except FileNotFoundError:  # 文件不存在
            with open('.\\file\\userinfo.pickle', 'wb') as file2:  # 准备创建新文件
                temple_us_info = {'admin': 'admin '}
                pickle.dump(temple_us_info, file2)

        if pas == com_pas:  # 两次密码输入一致
            if usname in us_info:  # 已经有该用户
                tk.messagebox.showerror(title='Error', message='The user has already signed up!')
            else:
                us_info[usname] = pas  # 在本地字典中增加元素
                with open('.\\file\\userinfo.pickle', 'wb') as file3:  # 将更新后的字典存储到文件中
                    pickle.dump(us_info, file3)
                    tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
                    signup_windows.destroy()
        else:  # 两次密码不一致
            tk.messagebox.showerror(title='Error', message='Password and confirm password must be the same!')
        signup_windows.destroy()  # 关闭子窗口

    def signup_cancel():  # 取消注册
        signup_windows.destroy()

    # 输入框变量
    texv1 = tk.StringVar()
    texv2 = tk.StringVar()
    texv3 = tk.StringVar()

    signup_windows = tk.Toplevel(windows)  # 在windows窗口上再建立一个子窗口
    signup_windows.geometry('100x200')
    signup_windows.title('Sign up')

    # 注册页面按钮
    tk.Label(signup_windows, text='User name').place(x=70, y=20)
    tk.Label(signup_windows, text='Password').place(x=70, y=40)
    tk.Label(signup_windows, text='Confirm your password').place(x=0, y=60)

    # 注册页面输入框
    tk.Entry(signup_windows, textvariable=texv1).place(x=145, y=20)
    tk.Entry(signup_windows, textvariable=texv2, show='*').place(x=145, y=40)
    tk.Entry(signup_windows, textvariable=texv3, show='*').place(x=145, y=60)

    # 注册页面按键
    tk.Button(signup_windows, text='OK', command=signup_ok).place(x=75, y=90)
    tk.Button(signup_windows, text='CANCEL', command=signup_cancel).place(x=120, y=90)


# sign up & sign in 按键
login_bt = tk.Button(windows, text='log in', command=usr_login).place(x=680, y=270)
signup_bt = tk.Button(windows, text='sign up', command=usr_signup).place(x=760, y=270)

windows.mainloop()

