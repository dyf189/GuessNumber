import re
temp = input('我们玩个游戏，猜一猜，这个数字是在1到20之间的:')
if re.match(r"^-?\d+$", temp):
    print("变量num是一个整数")
else:
    print("变量num不是一个整数")
