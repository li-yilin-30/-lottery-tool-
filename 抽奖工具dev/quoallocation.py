from tkinter import *
from tkinter.messagebox import showinfo
from siglottery import  *
from quick_lottery import *
from dif_lottery import  *
from ext_envelope import *
from double_ball import *
class quoallocation(object):
    def __init__(self,pagefirst):
        self.root=pagefirst
        self.root.geometry('600x340')
        self.superfirst = StringVar()
        self.first = StringVar()
        self.second= StringVar()
        self.third = StringVar()
        self.gold = StringVar()
        self.sliver= StringVar()
        self.num = StringVar()
        self.createchoosepage()

    def reconstruct(self):
        showinfo(title='success!', message='欢迎使用快速抽奖，下面将依次选出获奖者！')
        self.page.forget()
        quick_lottery(self.root)
        self.page.pack()
        #print(1)
    def reconstruct1(self):
        self.superfirst1=self.superfirst.get()
        self.first1 = self.first.get()
        self.second1 = self.second.get()
        self.third1 = self.third.get()
        self.gold1 = self.gold.get()
        self.sliver1 = self.sliver.get()
        if (len(self.first1)==0 or len(self.superfirst1)==0 or len(self.second1)==0 or len(self.third1)==0 or len(self.gold1)==0 or len(self.sliver1)==0):
            showinfo(title='fail!', message='请确保正确填写信息！')
        else:
            showinfo(title='success!', message='欢迎使用快速抽奖，下面将依次选出不同奖项！')
            self.page.forget()
            dif_lottery(self.root,self.superfirst1,self.first1,self.second1,self.third1,self.gold1,self.sliver1)
            self.page.pack()
        #print(1)
    def reconstruct2(self):
        if (len(self.num.get())==0):
            showinfo(title='fail!', message='请确保正确填写红包金额！')
        else:
            showinfo(title='success!', message='下面将进行红包抽取！')
            self.num2=int(self.num.get())
            self.page.forget()
            ext_envelope(self.root,self.num2)
            self.page.pack()

    def reconstruct3(self):
        #进入到双色球模式
        showinfo(title='success!', message='下面将模拟双色球！')
        self.page.forget()
        double_ball(self.root)
        self.page.pack()
        #print(1)
    def rereturn(self):
        showinfo(title='success!', message='返回模式选择！')
        self.page.destroy()
        patternchoose(self.root)


    def createchoosepage(self):
        #print(self.infoself)
        self.page = Frame(self.root)
        self.page.pack()
        label1=Label(self.page, text='奖项设置', font=("华文行楷", 15), anchor='w',fg="red")
        label1.place(anchor=NW, x=80, y=5)
        Label(self.page, text='', font=("华文行楷", 15)).grid(row=0, column=1)
        Label(self.page, text='特等奖',font=("华文行楷", 15)).grid(row=1, column=1)
        Entry(self.page, textvariable=self.superfirst).grid(
            row=1, column=2)
        Label(self.page, text='一等奖',font=("华文行楷", 15)).grid(row=2, column=1)
        Entry(self.page, textvariable=self.first).grid(
            row=2, column=2)
        Label(self.page, text='二等奖',font=("华文行楷", 15)).grid(row=3, column=1)
        Entry(self.page, textvariable=self.second).grid(
            row=3, column=2)
        Label(self.page, text='三等奖',font=("华文行楷", 15)).grid(row=4, column=1)
        Entry(self.page, textvariable=self.third).grid(
            row=4, column=2)
        Label(self.page, text='金卡会员权重',font=("华文行楷", 15)).grid(row=5, column=1)
        Entry(self.page, textvariable=self.gold).grid(
            row=5, column=2)
        Label(self.page, text='银卡会员权重',font=("华文行楷", 15)).grid(row=6, column=1,pady=5)
        Entry(self.page, textvariable=self.sliver).grid(
            row=6, column=2,pady=5)
        Label(self.page, text='红包金额', font=("华文行楷", 15)).grid(row=7, column=1)
        Entry(self.page, textvariable=self.num).grid(
            row=7, column=2)
        Button(self.page,text='快速模式',command=self.reconstruct).grid(row=8,column=1)
        Button(self.page, text='红包模式', command=self.reconstruct2).grid(row=8, column=3)
        Label(self.page, text='', font=("华文行楷", 15)).grid(row=9, column=1)
        Button(self.page, text='娱乐双色球', command=self.reconstruct3).grid(row=10, column=1)
        Button(self.page, text='设置完成', command=self.reconstruct1).grid(row=10,column=3)
        Button(self.page, text='返回', command=self.rereturn).grid(row=11, column=2)
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
        imgBtn2 = PhotoImage(file='4.png')
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
       # siglottery(self.root)
    def choose2(self):
        showinfo(title='success!', message='欢迎选择多人抽奖，下面将完成奖项设计！')
        self.page.destroy()
        #单人抽奖模式跳动到转盘的页面
        quoallocation(self.root)
