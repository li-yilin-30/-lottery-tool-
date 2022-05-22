import base64
from tkinter import  *
from tkinter.messagebox import showinfo
from patternchoose import *
from PIL import ImageTk, Image





def ff():
    return 1
class LoginUi(object):
    def __init__(self,pagefirst):
        self.root=pagefirst
        self.root.geometry('500x300')
        self.username = StringVar()
        self.password = StringVar()

        self.createpage()
    def createpage(self):
        self.page=Frame(self.root)
        self.page.pack()

        Label(self.page,text='用户名：').grid(row=1,stick=W,pady=15)
        Entry(self.page,textvariable=self.username).grid(row=1,column=1,stick=E)
        Label(self.page, text='密码：').grid(row=2, stick=W, pady=15)
        Entry(self.page, textvariable=self.password,show='*').grid(row=2, column=1, stick=E)
        Button(self.page,text='登录',command=self.logincheck).grid(row=3,stick=W,pady=15)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3,column=1)
        reg=Button(self.page, text='注册', command=self.check)
        #因为用户规模较小，这里就不再存储到数据库中，而是存储到同一目录下的txt中，点注册时写入到txt中，登录时从txt中读取并进行验证
        reg.place(anchor=NW, x=160, y=121)
        Label(self.page, text='欢迎使用抽奖工具！',font=("华文行楷", 20), fg="green",anchor ='center').grid(row=4, pady=15)
        Label(self.page, text='Good Luck！', font=("华文行楷", 20), fg="green", anchor='e').grid(row=5, pady=10)
    def logincheck(self):
        name=self.username.get()
        secret=self.password.get()
        flag= False
        with open('pwdandname.txt') as f:
            while (1):
                line1 = f.readline()
                line2 = f.readline()
                name1 = line1.rstrip()
                pwd1 = line2.rstrip()
                if(name1==''):
                    break
                if (name == name1):
                    #print(pwd1)
                   # print(type(pwd1))
                    pwdd=base64.b64decode(pwd1).decode("utf-8")
                    #print(pwdd)
                    if(pwdd!=secret):
                        continue
                    showinfo(title='success!', message='登录成功！')
                    self.page.destroy()
                    patternchoose(self.root)
                    flag=True
                    break
        if flag==False:
            showinfo(title='error!', message='请先申请使用资格！')


      #  if(name=='point'and secret=='123456'):
      #      self.page.destroy()
      #      showinfo(title='success!', message='正确！')
      #      patternchoose(self.root)
            #进入到模式选择的界面
      #  else:
      #      showinfo(title='error!',message='请先申请使用资格！')
    def check(self):
        with open('pwdandname.txt','a') as f:
           name = self.username.get()
           secret = self.password.get()
           byte_secret=secret.encode("utf-8")
           endcode_secret=base64.b64encode(byte_secret)
           temppasswd=str(endcode_secret)
           #print(temppasswd)
           f.write('\n'+name)
           f.write('\n'+temppasswd[2:-1])
           showinfo(title='success!', message='注册成功！')