# 如何使用数字、数字的用法
# 整数，小数

print(1024)
print(1.024)
print(-1024)

print(1+1)
print(1-1)
print(1*1)
print(1/1)

# 除法
## 整数除法 //  (双斜线)
print(8//5)

## 小数除法 /  (单斜线)
print(8/5)

# () 优先级
print((8+8)*5)

# 取余 % 求得整数除法后的余数

print(8%5)

# 有关数字的函数

## 1.str 将数字转化为字符串
number = 8
print("会打印出数字：" + str(number))

## 2.abs 取数字的绝对值
number = -8
print(abs(number))

## 3.pow(k,t)次方 k的t次方
print(pow(2,3)) # 2^3 = 8

## 4.max(······) 传几个数字都可以回传最大的数字
print(max(1,2,5,9,88,55,33,66,100))

## 5.min(······) 回传最小的数字
print(min(1,23,5,6,9,8,78,8,9,100))

## 6. round()  四舍五入
print(round(4.4))
print(round(4.5))

from math import *
from re import S
## 7. floor() 无条件舍去
print(floor(4.4))
print(floor(4.6))

## 8. ceil() 无条件进位
print(ceil(5.2))
print(ceil(5.8))

## 9. sqrt() 开根号
print(sqrt(64))
