# 建立一个基本的计算机
# 获得用户的输入 input()

# name = input("请输入你的名字：")
# print("Hello\n" + name)

from numpy import double


num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")
# input 把用户的输入默认当成字串来看

num1 = double(num1)
num2 = double(num2)
print(num1 + num2)
