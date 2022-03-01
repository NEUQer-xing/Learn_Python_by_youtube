# 猜数字游戏

secret = 77
guess = None
time = 0
f = False
while secret != guess:
    guess = int(input("请输入你猜的数字:"))
    time=time+1
    if(guess>secret):
        print("小一点")
    elif(guess<secret):
        print("大一点")
    else :
        f = True
    if(time==3 and f==False):
        print("次数已到,你输了!")
        break
if(f):
    print("你赢了!")