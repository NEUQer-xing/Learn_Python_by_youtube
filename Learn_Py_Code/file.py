# 文件的读取与存入

# open("文件路径",mode="开启模式")
# mode = 'r' 读取
# mode = 'w' 覆盖
# mode = 'a' 在原来的基础上加东西

file = open("Learn_Python_by_youtube/Learn_Py_Code/123.txt",mode="r")

for line in file:
    print(line)

files = file.read()

file_line = file.readline()

file_list = file.readlines()

print(type(files))
print(type(file_line))
print(type(file_list))
file.close()

file_w = open("Learn_Python_by_youtube/Learn_Py_Code/12.txt",mode = 'a',encoding="UTF-8")
file_w.write("\n你好")
file_w.close()

with open("Learn_Python_by_youtube/Learn_Py_Code/12.txt",mode = 'a',encoding="UTF-8") as file:
    file.write("哈哈,这样直接可以关闭")
    # 这样可以省去close