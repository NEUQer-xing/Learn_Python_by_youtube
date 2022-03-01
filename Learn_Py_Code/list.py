# 列表、列表的用法
#  创建列表
from re import T


score = [90,100,99,80,60]
print(score)

name = ["nike","xiao bai", " xiao ming"]
print(name)

things = [90,"xiao bai",True]
print(things)
# 打印正数第2位
print(things[1])
# 打印倒数第1位
print(things[-1])
# 打印正数第0-1位
print(things[0:2])
# 打印从第2个开始取到最后
print(things[1:])
# 打印从第3个开始到最开头
print(things[:3])

# list 的有关函数
score = [90,100,99,80,60]
name = ["nike","xiao bai","xiao ming"]
## 1.extend()   list 连接 
score.extend(name)
print(score)
## 2.append() 在list后添加元素
name.append("NEUQer_xing")
print(name)

## insert(index,val)
score.insert(2,30)
print(score)

## 4.remove(val)
score.remove(90)
print(score)

## 5.clear()
# score.clear()
# print(score)

## 6.pop()移除列表的最后一位
score.pop()

## 7.sort()由小到大

## 8.reverse() 反转

score.reverse()
print(score)

## 9 index(val)想要找的值,回传index
print(score.index(99))

## 10. count(val)计数: 统计在list中有几个val
print(score.count(99))
