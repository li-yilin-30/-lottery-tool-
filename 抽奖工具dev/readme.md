## 一个快捷使用的抽奖工具

```
使用方法：pip install requirements.txt 安装相关依赖后运行main.py
```

+ 自定义文件说明(这些文件需要您在抽奖前自行设置，是一些有关奖品、用户的可变信息)：
  + envelopusers.xlsx 输入分发红包的用户名
  + reward.xlsx 输入单人抽奖时奖品名单以及奖品获奖概率
  + users.xlsx 输入多人抽奖的用户名单，您可以通过用户姓名前添加(，标识为金卡会员，添加)标识为银卡会员。

+ 输出文件说明：
  + reward.txt是模拟双色球的中奖名单
  + pwdandname.txt base编码后管理用户的登录和注册

![image-20220522104313701](C:%5CUsers%5C50502%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20220522104313701.png)

多人抽奖说明：

+ 快速模式直接进行抽奖
+ 红包模式在填写红包金额后进行开红包
+ 点击娱乐双色球进入模拟双色球
+ 具体填写奖品数目和金银卡会员权重后，点击设置完成可以进入多人抽奖。