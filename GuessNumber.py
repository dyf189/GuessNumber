#小游戏
import random
import os
import time
from os import system
机会 = random.randint(4,8)
answer = random.randint(1,20)

system("title 猜数1.2Beta -by dyf189")

fw = open("last.txt","a")


#登录部分

print('登录猜数')
uesr = input('用户名:')

if os.path.exists('uesr.txt'):#第一层如果，检测是否存在“uesr.txt”
    with open('uesr.txt', 'r', encoding='utf-8') as f:
        usdata = f.readline()

        if uesr == usdata:#第二层如果，检测是否与用户名相同
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
    
#猜数部分

while 机会 > 0:
    temp = input('我们玩个游戏，猜一猜，这个数字是在1到20之间的:')
    guess = int(temp)

    if guess == answer:
        print('厉害啊，你是不是偷看代码了 good!')
        print('我先溜了，不玩了，别想要奖品')
        break
    else:
        if guess < answer:
            print('太小了，大胆一点')
        else:
            print('大了，小点')
        机会 = 机会 - 1

fw.write('\n结果是:' + str(answer))
print('游戏结束^_^Game Over^_^')
time.sleep(2)
print('----------------------------------')
print('剩余机会:', 机会)
print('答案:' , answer)
print('最后的回答:' , guess)
print('版本:1.2Beta')
print('----------------------------------')

numbers= [answer]

fw.close()
os.system('pause')

