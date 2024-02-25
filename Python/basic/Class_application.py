# program 1: roast a sweet potato
# 1. 定义类： 初始化属性，被烤和添加调料的方法，现实对象信息的str
class SweetPotato:
    # 定义一个初始状态
    def __init__(self):
        # 烤的时间
        self.cook_time = 0
        # 红薯状态
        self.potato_status = 'raw'
        # 调料列表
        self.seasoning = []

    def cook(self, time):
        # 先计算地瓜整体烤的时间
        self.cook_time += time
        # 用烤过的时间判断地瓜的状态
        if 0 <= self.cook_time < 3:
            self.potato_status = 'raw'
        elif 3 < self.cook_time < 5:
            self.potato_status = 'half cooked'
        elif 5 <= self.cook_time <= 8:
            self.potato_status = 'fulled cooked'
        elif self.cook_time > 8:
            self.potato_status = 'over cooked'

    def add_seasoning(self, seasoning):
        self.seasoning.append(seasoning)

    def __str__(self):
        return f'This sweet potato has been cooked for {self.cook_time} minutes, now it is {self.potato_status}' \
               f'we used these seasonings: {self.seasoning}'


# 2. 创建对象并调用对应的实例方法
sweet_potato_1 = SweetPotato()
print(sweet_potato_1)
sweet_potato_1.cook(3)
sweet_potato_1.cook(5)
sweet_potato_1.add_seasoning('sugar')
sweet_potato_1.add_seasoning('spices')
print(sweet_potato_1)
