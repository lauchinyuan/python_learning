import tkinter as tk

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小

lb = tk.Label(windows, text='Label').pack()

frm = tk.Frame(windows)  # 放置主框架
frm.pack()
frm_l = tk.Frame(frm)  # 左框架
frm_r = tk.Frame(frm)  # 右框架
frm_l.pack(side='left')  # 放置时选择左边放置
frm_r.pack(side='right')  # 放置在右边
lb_l = tk.Label(frm_l, text='On the left').pack()
lb_l2 = tk.Label(frm_l, text='On the left too').pack()
lb_r = tk.Label(frm_r, text='On the right').pack()

windows.mainloop()
