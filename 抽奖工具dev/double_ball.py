# coding=utf-8
import time
from tkinter import *
from tkinter import ttk
import random
import random,pymysql,time
from tkinter.messagebox import showinfo
imgBtn1 = None
class double_ball(object):
    def __init__(self, pagefirst):
        self.root = pagefirst
        self.root.geometry('600x340')
        self.var = StringVar()
        self.var.set("请选择模拟次数")
        #从数据库中读取数据
        self.id=[]
        self.red=[]
        self.blue=[]
        self.createchoosepage()
        #存储获奖名单
        self.firstid = []
        self.secondid = []
        self.thirdid = []
        self.fourthid = []
        self.fifthid = []
        self.sixthid =[]



    def reconstruct(self):
        showinfo(title='success!', message='即将返回到设置页面！')
        self.page.destroy()
    def lottery_start(self):
        try:
            num=int(self.var.get())
            print(num)
            self.generate_ball(num)
            showinfo(title='success!', message='成功向数据库中添加'+str(num)+'条投注信息')
        except:
            showinfo(title='fault!', message='请先选择投注人数')
        red_balls1 = [self.add0(x) for x in range(1, 34)]
        blue_balls1= [self.add0(x) for x in range(1, 17)]
        while True:
            red_num1 = random.sample(red_balls1, 6)
            setlist = set(red_num1)  # 随机生成6位不重复红球list
            if len(setlist) == len(red_num1):
                break
        #red_num1 = random.sample(red_balls1, 6)  # 随机生成6位红球list
        blue_num1= random.sample(blue_balls1, 1)
        self.a='本期中奖号码为:'+str(red_num1[0])+','+str(red_num1[1])+','+str(red_num1[2])+','+str(red_num1[3])+','+str(red_num1[4])+','+str(red_num1[5])+','+str(blue_num1[0])
        self.b=str(red_num1[0])+','+str(red_num1[1])+','+str(red_num1[2])+','+str(red_num1[3])+','+str(red_num1[4])+','+str(red_num1[5])
        self.c=str(blue_num1[0])
        print(self.b)
        print(self.c)
        self.show_label.configure(text=self.a)
        self.judge()
        showinfo(title='success!', message='获奖名单已经写入到了reward.txt！')
        with open("reward.txt",'w') as f:
            f.write("一等奖"+'\n')
            for i in self.firstid:
                f.write(str(i))
                f.write(' ')
            f.write('\n')
            f.write("二等奖"+'\n')
            for i in self.secondid:
                f.write(str(i))
                f.write(' ')
            f.write('\n')
            f.write("三等奖"+'\n')
            for i in self.thirdid:
                f.write(str(i))
                f.write(' ')
            f.write('\n')
            f.write("四等奖"+'\n')
            for i in self.fourthid:
                f.write(str(i))
                f.write(' ')
            f.write('\n')
            f.write("五等奖" + '\n')
            for i in self.fifthid:
                f.write(str(i))
                f.write(' ')
            f.write('\n')
            f.write("六等奖"+'\n')
            for i in self.sixthid:
                f.write(str(i))
                f.write(' ')


    def judge(self):

        myconnect2 = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, db='sakila',
                                    charset='utf8')
        cur = myconnect2.cursor()
        sql1 = "select * from datas"
        cur.execute(sql1)
        results = cur.fetchall()
        for row in results:
            self.id.append(row[0])
            self.red.append(row[1])
            self.blue.append(row[2])
        myconnect2.commit()
        cur.close()
        myconnect2.close()
        print(self.id)
        print(self.red)
        print(self.blue)
        self.judge_reward(self.id,self.red,self.blue,self.b,self.c)
        print(self.firstid)
        print(self.secondid)
        print(self.thirdid)
        print(self.fourthid)
        print(self.fifthid)
        print(self.sixthid)
    def judge_reward(self,a,b,c,d,e):
        for i in range(len(a)):
            print(i)
            print(b[i])
            print(d)
            num1= self.judge1(b[i],d)
            print(num1)
            num2= self.judge2(c[i],e)
            if(num1==6 and num2==1):
                self.firstid.append(a[i])
            elif(num1==6 and num2==0):
                self.secondid.append(a[i])
            elif (num1 == 5 and num2 == 1):
                self.thirdid.append(a[i])
            elif (num1 == 5 and num2 == 0)or(num1 == 4 and num2 == 1):
                self.fourthid.append(a[i])
            elif (num1 == 4 and num2 == 0) or (num1 == 3 and num2 == 1):
                self.fifthid.append(a[i])
            elif (num1 == 0 and num2 == 1) :
                self.sixthid.append(a[i])
            else:
                continue
    def judge1(self,x,y):
        num=0
        for i in range(6):
            #print(i)
           # print(x[3 * i])
           # print(y[3 * i])
           # print(x[3 * i + 1])
           # print(y[3 * i + 1])
            if (x[3*i]==y[0] and x[3*i+1]==y[1]) or(x[3*i]==y[3] and x[3*i+1]==y[4])or(x[3*i]==y[6] and x[3*i+1]==y[7])or(x[3*i]==y[9] and x[3*i+1]==y[10])or(x[3*i]==y[12] and x[3*i+1]==y[13])or(x[3*i]==y[15] and x[3*i+1]==y[16]):

              #  print(x[3*i])
               # print(y[3*i])
               # print(x[3*i+1])
               # print(y[3 * i + 1])

                num=num+1
        return num
    def judge2(self,x,y):
        num=0
       # print(x[0])
       # print(y[0])
       # print(x[1])
       # print(y[1])
        if x[0]==y[0] and x[1]==y[1]:
           # print(x[0])
           # print(y[0])
           # print(x[1])
           # print(y[1])
            num=num+1
        return num


    def createchoosepage(self):
        self.page = Frame(self.root)
        self.page.pack()
        #保证可以正常显示
        Label(self.page, width=70, height=24, bg='#ECf5FF').grid(row=0)
        w = OptionMenu(self.page,self.var, "100", "1000", "10000","100000")

        w.place(anchor=NW, x=190, y=150)
        button1 = Button(self.page, text='开始', command=self.lottery_start, width=4, height=1,
                         bg='#A8A8A8',
                         font='宋体 -18 bold')
        button1.place(anchor=NW, x=180, y=200)
        button2 = Button(self.page, text='返回', command=self.reconstruct, width=4, height=1,
                         bg='#A8A8A8',
                         font='宋体 -18 bold')
        button2.place(anchor=NW, x=260, y=200)

        self.show_label = Label(self.page, text='请点击开始按钮进行抽奖',  anchor=CENTER, width=40, height=1, bg='#ECf5FF',
                            font='宋体 -15 bold', foreground='red')
        self.show_label.place(anchor=NW, x=110, y=100)
        myconnect1 = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, db='sakila', charset='utf8')
        cur1 = myconnect1.cursor()
        sql0 = "delete from datas"
        cur1.execute(sql0)  # 批量执行
        myconnect1.commit()
        cur1.close()
        myconnect1.close()

    def generate_ball(self,count):
        red_ball = self.add0(random.randint(1, 34))
        blue_ball = self.add0(random.randint(1, 17))
        red_balls = [self.add0(x) for x in range(1, 34)]
        blue_balls = [self.add0(x) for x in range(1, 17)]
        ball_list = []
        for i in range(count):

            while True:
                  red_num = random.sample(red_balls, 6)
                  setlist=set(red_num)# 随机生成6位不重复红球list
                  if len(setlist)==len(red_num):
                      break
            #print(red_num)
            blue_num = random.sample(blue_balls, 1)
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S')  # 当前时间格式化
            ball = (i+1,','.join(red_num), blue_num,cur_time)  # 将红，蓝球，时间加入元祖
            ball_list.append(ball)
        #self.clearmysql()
        print(len(ball_list))
        self.into_mysql(ball_list)
    def add0(self,num):
        #双色球序号有0开头的
        if num in range(1, 10):
            num = str(num)
            new_num = '0' + num
        else:
            new_num = str(num)
        return new_num

    def into_mysql(self,ball_list):
        myconnect = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, db='sakila', charset='utf8')
        cur = myconnect.cursor()
        sql = "insert into datas(id,red,blue,date) values(%s,%s,%s,%s)"
        cur.executemany(sql, ball_list)  # 批量执行
        myconnect.commit()
        cur.close()
        myconnect.close()


