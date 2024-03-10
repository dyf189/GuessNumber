#小游戏
import random
import os
import time
import re
from os import system
from colorama import Fore, Back, Style, init

system("title 猜数1.4Beta -by dyf189")
#初始colorama
init()
#初始猜数模式
难度 = '简单'
最高 = '20'
#打开上一次文件
fw = open("last.txt","a")
#将模式默认
test = 'false'
mode = 'lx'

#系统检测部分

系统 = os.name
if 系统 == 'nt':
    系统 = 'win'
elif 系统 == 'win32':#win32
      系统 = 'win'
elif 系统 == 'win64':
      系统 = 'win'
elif 系统 == 'linux':
      系统 = 'GNU'
else:
   print('抱歉，您的系统不支持猜数。')
   time.sleep(3)
   exit()

#登录部分

print('登录猜数')
uesr = input('用户名:')

if os.path.exists('uesr.txt'):#第一层如果，检测是否存在“uesr.txt”
    with open('uesr.txt', 'r', encoding='utf-8') as f:
        usdata = f.readline()

        if uesr == usdata:#第二层如果，检测是否与用户名相同
            if usdata == '':
                print('空用户名将会导致无法在线游玩')
            else:
                pass
            password = input('密码:')
            if os.path.exists('password.txt'):#第三层，检测是否存在“password.txt”
                with open('password.txt', 'r', encoding='utf-8') as pw:
                    pwdata = pw.readline()

                    if password == pwdata:#第四层，检测password.txt是否与输入内容一致
                       print('欢迎进入猜数')
                    else:
                       print('密码不正确')
                       os.system('pause')
                       exit()
            else:
                with open('password.txt',mode="a",encoding='utf-8') as pw:#如果不存在，创建password.txt并关闭程序（重启）
                    pw.write('12345678')
                    print('未检测到文件，正在创建中......请重启猜数')
                    time.sleep(2)
                    exit()
        else:
            print('此用户名不存在')
            os.system('pause')
            exit()
else:
    with open("uesr.txt", mode='a', encoding='utf-8') as f:
        f.write('admin')
        print('未检测到文件，正在创建中......请重启猜数')
        time.sleep(2)
        exit()


#选择部分
while True:
    temp = input('_____________________________________\n 请选择模式：\n 1：游玩 2：查看记录 3：用户数据 4:切换游戏难度\n如果不想登录或不想看到此消息？请输入5\n空格默认为1\n6:在线游玩\n')
    if temp == '1':
        break
    elif temp == '2':
        print('抱歉，功能未实现')
    elif temp == '3':#查看用户数据，可修改密码、用户名
        print('用户名:' , usdata , '\n密码:', pwdata)
        temp = input('修改密码请输入1\n修改用户名请输入2\n空格默认进行游玩\n')
        if temp == '1':
          temp = input('请输入密码:')
          print('修改成功！')
          with open('password.txt', 'w', encoding='utf-8') as pw:
              pw.write(temp)
        elif temp == '2':
            temp = input('请输入用户名')
            print('修改成功！')
            with open('uesr.txt', 'w', encoding='utf-8') as f:
                f.write(temp)
        else:
            break
    elif temp == '4':
        temp = input('简单：随机数1-20，4-8次机会\n普通：随机数1-50，10-14次机会\n困难：随机数1-100，18-24次机会\n默认简单，请输入难度代表数字：')
        if temp == '1':
            难度 = '简单'
        elif temp == '2':
              难度 = '普通'
        elif temp == '3':
              难度 = '困难'
    elif temp =='5':
        print('抱歉，功能未实现')
    elif temp == '6':
        mode = 'Web'
        import GuessNumberWeb
    elif temp == '114':
        test = 'true'
        print('已开启调试模式')
    else:
        break


#猜数部分
if 难度 == '简单':
  机会 = random.randint(4,8)
  answer = random.randint(1,20)
  最高 ='20'
elif 难度 == '普通':
    机会 = random.randint(10,14)
    answer = random.randint(1,50)
    最高 = '50' 
elif 难度 ==  '困难':
    机会 = random.randint(18,24)
    answer = random.randint(1,100)
    最高 = '100'
elif 难度 == '彩蛋':
    机会 = random.randint(1,100)
    answer = random.randint(114514,200000)

if mode == 'Web':
  GuessNumberWeb.dl(usdata)
  GuessNumberWeb.nd('1','20')
  


jihui = 机会
while 机会 > 0:
    if 机会 == jihui:
      temp = input('我们玩个游戏，猜一猜，这个数字是在1到' + str(最高) + '之间的：')#初始化，输入数值以猜测
    else:
        temp = input('请输入一个数：')


    if re.match(r"^-?\d+$", temp):#判断是否为整数值，如果是，进行判断
        guess = int(temp)

        if guess == answer:
            结果文字 = random.randint(1,3)
            if 结果文字 == 1:
              print('厉害啊，你是不是偷看代码了 good!')
              print('我先溜了，不玩了，别想要奖品')
              break
            elif 结果文字 == 2:
                print('游戏结束了，恭喜你猜对了!')
                break
            elif 结果文字 == 3:
                print('Game Over.\nThank you play this game.')
                break
        else:
            if guess < answer:
                print('太小了，大胆一点')
                机会 = 机会-1
            else:
                print('大了，小点')
                机会 = 机会 - 1
    else:#否则进行提示，并结束本次循环
        print('请输入一个整数')
        continue


#结尾清算部分

fw.write('\n结果是:' + str(answer))
fw.close()

print('游戏结束^_^Game Over^_^')
time.sleep(2)
print('----------------------------------')
print('剩余机会:', 机会)
print('答案:' , answer)
print('最后的回答:' , guess)
print('版本:1.4Beta')
print('----------------------------------')

#结尾等待部分

if 系统 == 'win':
    os.system('pause')
elif 系统 == 'GNU':
    os.system('sleep 5')
else:
    exit()



