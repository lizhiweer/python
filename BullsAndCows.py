# 猜数字
import random

num = random.randint(1, 20)

print("请输入一个一到20的整数")

while True:
    print("请输入猜测的数字:")
    guss = int(input())
    if guss > num:
        print("您输入的值太大了")
    elif guss < num:
        print("您输入的值太小了")
    else:
        print("恭喜您猜对了")
        break
