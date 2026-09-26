# 魔法方法：__str__打印时调用，__lt__比较时调用
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):        # print(实例) 时调用
        return f'{self.name}({self.age})'

    def __lt__(self, other):  # < 比较时调用
        return self.age < other.age

p1 = Person('张三', 18)
p2 = Person('李四', 20)
print(p1)          # 张三(18)
print(p1 < p2)     # True
