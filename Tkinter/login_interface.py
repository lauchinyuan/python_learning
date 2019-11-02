# tkinter的综合应用，设计登录窗口
import tkinter as tk

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


def usr_signup():
    pass


login_bt = tk.Button(windows, text='log in', command=usr_login).place(x=680, y=270)
signup_bt = tk.Button(windows, text='sign up', command=usr_signup).place(x=760, y=270)

windows.mainloop()

