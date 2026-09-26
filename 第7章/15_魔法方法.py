# 魔法方法：双下划线开头结尾，Python 自动调用
#
# ⚠️ Java vs Python 差异：
#   Java：toString() → System.out.println(p) 自动调
#   Python：__str__() → print(p) 自动调
#
#   Java：equals() → a.equals(b)
#   Python：__eq__() → a == b
#
#   常见魔法方法：
#   __init__ 构造  __str__打印  __len__len()  __lt__<比较  __eq__==比较

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):        # 相当于 Java 的 toString()
        return f'{self.name}({self.age})'

    def __lt__(self, other):  # 相当于 Java 的 Comparable
        return self.age < other.age

p1 = Person('张三', 18)
p2 = Person('李四', 20)
print(p1)          # 自动调 __str__
print(p1 < p2)     # 自动调 __lt__
