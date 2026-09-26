# 类定义：class类名，__init__构造方法初始化属性
class Person:
    # __init__ 构造方法：创建实例时自动调用，初始化属性
    def __init__(self, name, age):
        self.name = name   # self.属性 = 值，给实例加属性
        self.age = age
