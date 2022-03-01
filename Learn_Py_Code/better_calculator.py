# 设计一个计算器

num1 = float(input("请输入第一个数字:"))
op = input("请输入运算符:")
num2 = float(input("请输入第二个数字:"))
ans = 0
f = True
if op=='+':
    ans = num1 + num2
elif op == '-':
    ans = num1 - num2
elif op == '*':
    ans = num1 * num2
elif op == '/':
    ans = num1 / num2
else :
    f = False
    print("无法运算!!!")
if f==True:
    print("计算结果为" + str(ans))