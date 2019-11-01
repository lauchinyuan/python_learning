# tkinter的综合应用，设计登录窗口
import tkinter as tk

windows = tk.Tk()  # 注意是Tk
windows.title('tkinter')
windows.geometry('100x200')  # 设定窗口大小

cav = tk.Canvas(windows, bg='white', width=280, height=180)
photo_file = tk.PhotoImage(file='.\\image\\github logo.png')
cav.create_image(0, 0, anchor='nw', image=photo_file)
cav.pack()
windows.mainloop()

