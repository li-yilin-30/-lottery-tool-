# coding=utf-8
import time
from tkinter import *
import random
from tkinter.messagebox import showinfo


data1=[]
going = True
is_run = False
class quick_lottery(object):
    def __init__(self, pagefirst):
        self.root = pagefirst
        self.root.geometry('600x340')
        self.v1=StringVar()
        self.v2 = StringVar()
        #self.num=num
        self.user=self.fromxlxs()
        self.createchoosepage()

    def reconstruct(self):
        showinfo(title='success!', message='即将返回到设置页面！')
        self.page.destroy()

    def fromxlxs(self):
        import xlrd
        # from xlwt import *
        # 读取奖品名单
        fileName = "users.xlsx"

        book = xlrd.open_workbook(fileName)
        # 读取表1
        try:
            sheet = book.sheet_by_name("Sheet1")
        except:
            print("请确保excel中sheet1表存在")

        nrows = sheet.nrows  # 获取行数
        # 读取第一列的数据，存储着奖品名称
        ans = []
        for i in range(0, nrows):
            row_data = sheet.row_values(i)
            ans.append(row_data)


        return ans
    def createchoosepage(self):
        self.page = Frame(self.root)
        self.page.pack()
        print(self.user)
        #这个标签仅仅用于占位显示，不然会出现一片空白
        Label(self.page, width=70, height=24, bg='#ECf5FF').grid(row=0)
        self.v1=StringVar(value='ready！')
        show_label1 = Label(self.page, textvariable=self.v1, justify='left', anchor=CENTER, width=17, height=3, bg='#BFEFFF',
                            font='华文行楷 -40 bold', foreground='black')
        self.v2=StringVar(value='即将抽奖')
        show_label1.place(anchor=NW, x=24, y=20)
        show_label2 = Label(self.page, textvariable=self.v2, justify='left', anchor=CENTER, width=38, height=3, bg='#ECf5FF',
                            font='华文行楷 -18 bold', foreground='red')
        show_label2.place(anchor=NW, x=21, y=240)

        button1 = Button(self.page, text='开始', command=lambda: self.lottery_start(self.v1, self.v2), width=14, height=2, bg='#A8A8A8',
                         font='华文行楷 -18 bold')
        button1.place(anchor=NW, x=20, y=175)
        button2 = Button(self.page, text='结束', command=lambda: self.lottery_end(), width=14, height=2, bg='#A8A8A8',
                         font='华文行楷 -18 bold')
        button2.place(anchor=NW, x=232, y=175)
        button3 = Button(self.page, text='返回', command=lambda: self.reconstruct(), width=10, height=2, bg='#A8A8A8',
                         font='华文行楷 -18 bold')
        button3.place(anchor=NW, x=420, y=250)
        self.theLB = Listbox(self.page, selectmode=MULTIPLE, height=11,width=8)

        self.theLB.place(anchor=NW, x=430, y=15)

    def lottery_roll(self,var1, var2):
        global going
        luckmember = random.choice(data1)
        var1.set(luckmember)
        #print(going)
        if going:
            #print('@')
            self.page.after(10, self.lottery_roll, var1, var2)
            #print('@')
        else:
            var2.set('恭喜 {} ！成功抽到了奖品'.format(luckmember))
            self.theLB.insert(END,luckmember)
            showinfo(title='good!', message='恭喜 {} ！成功抽到了奖品'.format(luckmember))
            going = True
            return

    def lottery_start(self,var1, var2):
        #print(type(self.user[0][0]))
        for i in range(len(self.user)):
            data1.append(self.user[i][0])
        #print(data1)
        global is_run
        #print(going)
        #print(is_run)
        is_run=False
        if is_run:
            return
        is_run = True
        var2.set('快速抽奖ing')
        self.lottery_roll(var1, var2)

    def lottery_end(self):
        global going, is_run
        if is_run:
            going = False
            is_run = False



