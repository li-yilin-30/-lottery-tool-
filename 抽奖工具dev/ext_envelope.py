# coding=utf-8
import time
from tkinter import *
import random
from tkinter.messagebox import showinfo
imgBtn1 = None
class ext_envelope(object):
    def __init__(self, pagefirst,x):
        self.root = pagefirst
        self.root.geometry('600x340')
        self.user=self.fromxlxs()
        self.numofuser=len(self.user)
        self.createchoosepage()
        self.result=[]
        self.total=x

    def reconstruct(self):
        showinfo(title='success!', message='即将返回到设置页面！')
        self.page.destroy()

    def fromxlxs(self):
        import xlrd
        # from xlwt import *
        # 读取奖品名单
        fileName = "envelopeusers.xlsx"

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
        global imgBtn1
        imgBtn1 = PhotoImage(file='6.png')
        #保证可以正常显示
        Label(self.page, width=70, height=24, bg='#ECf5FF').grid(row=0)
        btn1=Button(self.page, text='单人抽奖', height=300, width=300, command=self.choose, image=imgBtn1)
        btn1.place(anchor=NW, x=0, y=20)
        btn1=Button(self.page, text='返回', height=2, width=6, command=self.reconstruct)
        btn1.place(anchor=NW, x=435, y=280)
        show_label = Label(self.page, text='金额分配',  anchor=CENTER, width=38, height=3, bg='#ECf5FF',
                            font='华文行楷 -15 bold', foreground='red')
        show_label.place(anchor=NW, x=303, y=3)
        self.theLB = Listbox(self.page, selectmode=MULTIPLE, height=11,width=15)

        self.theLB.place(anchor=NW, x=380, y=60)
    def choose1(self,i,x):
        # 最后一位，获得剩下所有红包
            if i == 1:
                self.result.append(self.total-sum(self.result))
                return self.result

            #获取0.01 ~ 剩余红包均值*2 的随机值
            max_num = ((self.total - sum(self.result)) / i) * 2
            tmp_money = random.uniform(0.1, max_num)
            self.result.append(tmp_money)

            return self.choose1(i - 1, self.result)
    def choose(self):
        self.choose1(self.numofuser,self.result)
        print(self.result)
        for i in range(self.numofuser):
            self.theLB.insert(END, self.user[i][0]+' '+str(round(self.result[i],2)))
        showinfo(title='success!', message='红包抽取完毕！')


