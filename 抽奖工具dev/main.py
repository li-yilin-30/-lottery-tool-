from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk
style = Style(theme='journal')
style.configure('TLabel',foreground='red')
from LoginUi import *
#root =Tk()
root=style.master
root.title('抽奖工具')
root.geometry('300x300')
root.resizable(0,0)
LoginUi(root)

root.mainloop()