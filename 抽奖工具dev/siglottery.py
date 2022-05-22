#encoding=utf-8
from tkinter import *
from tkinter.messagebox import showinfo
#from LoginUi import *
#from patternchoose import *
from quoallocation import  *
import random
is_run = False
tmp=None
class siglottery(object):
    def __init__(self,pagefirst):
        self.root=pagefirst
        self.root.geometry('520x370')
        global  tmp
        tmp=self.root
        self.infoself=self.fromxlxs()

       # print(type(self.infoself[0]))
       #  a='字符'
       # print(type(a))
        self.createchoosepage()
    def fromxlxs(self):
        import xlrd
        # from xlwt import *
        # 读取奖品名单
        fileName = "reward.xlsx"

        book = xlrd.open_workbook(fileName)
        # 读取表1
        try:
            sheet = book.sheet_by_name("Sheet1")
        except:
            print("请确保excel中sheet1表存在")

        nrows = sheet.nrows  # 获取行数
        # 读取第一列的数据，存储着奖品名称
        ans = []
        ans1 = []
        for i in range(0, nrows):
            row_data = sheet.row_values(i)
            ans.append(row_data)


        return ans
    #定义轮盘相关的信息
    def whirl_speed_control(self, data, i, number,z):
        #具体的抽奖过程逻辑分离，通过ramdom确定到底抽到哪一个，在通过速度逐渐变缓慢定位到要抽中的
        #那个奖品
        global is_run
        if is_run==False:
            return
        if i == 0:
            j = 0
        else:
            j = i % 8
        data[j - 1]['bg'] = '#CCCCCC'
        data[j]['bg'] = '#00CD00'
        wait=[10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]
        if i < number:
            #print(wait[i])
            self.root.after(wait[i], self.whirl_speed_control, data, i + 1, number,z)
        else:
            #print(i)
            #print(i%8)
            #print(z)
            if i%8==z:
                is_run = False
                showinfo(title='congratulate!', message='恭喜抽到了'+data[z]['text']+'!')
            self.root.after(wait[i], self.whirl_speed_control, data, i + 1, number, z)

    def lot_start(self,data):
        global is_run
        if is_run:
            return
        is_run = True
        tmp=[]
        for i in range(len(self.infoself)):
            k=0
            for j in range(int(1000*self.infoself[i][1])):
                tmp.append(i)
                k=k+1
           # print(k)
        #print(tmp)
        num=random.randint(0,999)
        #print(num)
        print(len(tmp))
        #datachoose=data[tmp[num]]
        # print(datachoose)
        for x in range(len(data) - 1):
            data[x]['bg'] = '#CCCCCC'
        number = random.randint(20, 30)
        #print(tmp[num])
        self.whirl_speed_control(data, 0, number,tmp[num])
    #根据位置构建奖项标签
    def makelab_forpos(self, name, x, y):
        label = Label(self.root, text=name, width=13, height=3, bg='#CCCCCC', font='华文行楷 -20 ')
        label.place(anchor=NW, x=x, y=y)
        return label
    def reconstruct(self):
        showinfo(title='success!', message='欢迎使用转盘模式！')

        patternchoose(self.root)

    def createchoosepage(self):
        #print(self.infoself)

        if(len(self.infoself)!=8):
            i=len(self.infoself)-1
            while i<8:
                self.infoself.append(('空奖项').split())
                #print(i)
                i=i+1
        #print(self.infoself)
        label1 = self.makelab_forpos(str(self.infoself[0][0]), 20, 20)
        label2 = self.makelab_forpos(str(self.infoself[1][0]), 180, 20)
        label3 = self.makelab_forpos(str(self.infoself[2][0]), 340, 20)
        label4 = self.makelab_forpos(str(self.infoself[3][0]), 20, 110)
        label5 = self.makelab_forpos(str(self.infoself[4][0]), 340, 110)
        label6 = self.makelab_forpos(str(self.infoself[5][0]), 20, 200)
        label7 = self.makelab_forpos(str(self.infoself[6][0]), 180, 200)
        label8 = self.makelab_forpos(str(self.infoself[7][0]), 340, 200)
        #data 用于存储奖品
        data = [label1, label2, label3, label5, label8, label7, label6, label4]
        #开始按钮
        #print('hello')
        button_start = Button(self.root, text='开   始', command=lambda: self.lot_start(data), width=115, height=60,
                             bg='#ff9900',font='华文行楷 -20', bitmap='gray50', compound=CENTER)
        button_start.place(anchor=NW, x=180, y=110)
        button_return = Button(self.root, text='返回', command=lambda:{label1.destroy(),label2.destroy(),label3.destroy(),label4.destroy(),label5.destroy(),label6.destroy(),label7.destroy(),label8.destroy(),button_return.destroy(),button_start.destroy(),patternchoose(self.root)}
                               , width=17, height=3,
                             bg='#ff9900',font='华文行楷 -20',  compound=CENTER)
        button_return.place(anchor=NW, x=160, y=280)
       # print(self.infoself)

        # 单人抽奖模式跳动到转盘的页面
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

