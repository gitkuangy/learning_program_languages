# define a class use the class to create an object

# define a class
class DishWasher:
    # 初始化属性
    # def __init__(self):
    #   self.width = 200
    #   self.height = 800
    # 带参数的初始化属性
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'explanation of this Class'  # 如果打印对象，本来打印的是对象内存地址，现在可以打印此返回值

    def __del__(self):
        print('delete every thing')  # 删除整个

    def wash(self):
        print('wash the dishes')

    # 类内添加和获取对象属性
    def print_info(self):
        print(f"dishwasher's width is {self.width}")
        print(f"dishwasher's width is {self.height}")


# create an object
samsung = DishWasher(20, 30)  # 用类创建对象
samsung.wash()  # 对象调用类里的功能
kitchen_aid = DishWasher(40, 50)
kitchen_aid.wash()

# 添加和获取对象属性及其value
# 类外添加和获取对象属性   对象名.属性名 = value
# samsung.width = 300
# samsung.height = 500

samsung.print_info()
kitchen_aid.print_info()
