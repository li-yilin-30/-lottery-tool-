# -*- coding: utf-8 -*-
from tkinter import  *
from siglottery import  *
from quoallocation import  *
from tkinter.messagebox import showinfo
imgBtn1 = None
imgBtn2 = None
#共分为单人抽奖模式与多人抽奖的模式，单人模式需要通过
#reward.xlxs导入奖品，多人模式需要导入奖品分配比例与参与者信息
class patternchoose(object):
    def __init__(self,pagefirst):
        self.root=pagefirst
        self.root.geometry('600x400')
        self.createchoosepage()
    def createchoosepage(self):
        self.page = Frame(self.root)
        self.page.pack()
        global  imgBtn1
        global imgBtn2

        imgBtn1 = PhotoImage(file='3.png')
        imgBtn2 = PhotoImage(file='9.png')
        Label(self.page, text='', font=("华文行楷", 15), fg="red", anchor='w').grid( column=0,pady=10)
        Button(self.page, text='单人抽奖', height=200,width=200,command=self.choose1,image=imgBtn1).grid(row=1, stick=W, pady=15)
        Button(self.page, text='单人抽奖', height=200, width=200, command=self.choose2, image=imgBtn2).grid(row=1,column=1, stick=E,pady=15)
        label1=Label(self.page, text='单人抽奖', font=("华文行楷", 15), anchor='w',fg="red")
        label1.place(anchor=NW, x=60, y=280)
        label2 = Label(self.page, text='多人抽奖', font=("华文行楷", 15), anchor='w', fg="red")
        label2.place(anchor=NW, x=260, y=280)
        label3 = Label(self.page, text='模式选择', font=("华文行楷", 15), anchor='w', fg="red")
        label3.place(anchor=NW, x=170, y=20)
        Label(self.page, text='', font=("华文行楷", 15),  anchor='e',fg="red").grid(row=2,column=1,stick=W,pady=20)
        #  button1.pack()
    def choose1(self):
        showinfo(title='success!', message='欢迎使用转盘模式！')
        self.page.destroy()
        #单人抽奖模式跳动到转盘的页面
        siglottery(self.root)
    def choose2(self):
        showinfo(title='success!', message='欢迎选择多人抽奖，下面将完成奖项设计！')
        self.page.destroy()
        #单人抽奖模式跳动到转盘的页面
        quoallocation(self.root)
      #  self.page.pack()
