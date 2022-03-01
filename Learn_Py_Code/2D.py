# 二维列表 
nums = [
    [1,2,3],
    [4,5,6],
    [7],
    [8],
    [9]]
for row in nums:
    print(str(type(row))+'    '+ str(row))
    for col in row:
        print(str(type(col))+"      "+ str(col))

