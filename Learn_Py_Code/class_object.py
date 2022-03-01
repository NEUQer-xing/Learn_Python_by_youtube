# 类  对象
# 类别 物件
# class object
class phone:
    def __init__(self,os,number,is_water):
        self.os = os
        self.number = number
        self.is_water = True
    def is_ios(self):
        if self.os =='ios':
            return True
        else:
            return False
    # 有关类里面的函数,第一个传入的参数就是self
phone1 = phone("ios",123,True)

print(phone1)