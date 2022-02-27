#如何使用字串、子串的用法
# 换行 \n
print("hello\nNEUQer")

# 字串里有字符 \ + 字符：\表示是转义字符
print("hello\"NEUQer")

# + 
print("hello" + "NEUQ")

# lower() 全部转为小写
str = "Hello NEUQer"
print(str.lower())

# upper() 全部转为大写
print(str.upper())

# isupper() 是否全是大写：是 true 不是 false
# islower() 是否全是小写：是 true 不是 false

print(str.isupper())
print(str.islower())

# 函数可以叠加

print(str.lower().islower())
print(str.upper().isupper())

# 输出子串里的单独一个字符
print(str[0]) 
# Hello NEUQer
# 0123456789··

# 找到字符串里的某个字符的位置
# 若匹配的字符有很多，返回第一个匹配的字符
print(str.index('H'))

# 字符串中字符的替换 第一个：要替换的字符 第二个：替换之后的字符
# Hello NEUQer
print(str.replace('H','h'))
# hello NEUQer