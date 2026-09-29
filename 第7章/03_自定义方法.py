# 学习目标：三种方法类型：实例方法类方法静态方法
#
# 类方法的三种类型：实例方法 / 类方法 / 静态方法
#
# ⚠️ Java vs Python 差异：
#   Java：成员方法 vs static 方法
#   Python：分三种，区别在第一个参数
#
# ┌──────────┬─────────────┬──────────┬─────────────────┐
# │ 类型     │ 装饰器      │ 首参数   │ 相当于 Java 的  │
# ├──────────┼─────────────┼──────────┼─────────────────┤
# │ 实例方法 │ 无          │ self     │ 普通成员方法    │
# │ 类方法   │ @classmethod│ cls      │ static 方法     │
# │ 静态方法 │ @staticmethod│ 无     │ static 工具函数 │
# └──────────┴─────────────┴──────────┴─────────────────┘
#
# self 相当于 Java 的 this，但：
#   - Java 的 this 是隐式的，不用写在参数列表里
#   - Python 的 self 必须写在第一个参数位置！
#   - 调用时 p.speak("hi")，Python 自动把 p 传给 self，不用手动传

class Person:  # ⭐ 定义类
    count = 0   # 类属性

    def __init__(self, name):  # ⭐ 类方法
        self.name = name

    # ① 实例方法：操作实例属性，第一个参数 self
    def speak(self, msg):  # ⭐ 类方法
        print(f'我叫{self.name}，{msg}')

    # ② 类方法：操作类属性，第一个参数 cls
    @classmethod
    def add_count(cls):  # ⭐ 类方法
        cls.count += 1

    # ③ 静态方法：不操作实例也不操作类，没有 self/cls
    @staticmethod
    def is_adult(age):  # ⭐ 类方法
        return age >= 18


p = Person('张三')
p.speak('你好')         # 实例方法：自动传 p 给 self
Person.add_count()      # 类方法：自动传 Person 给 cls
print(Person.is_adult(18))  # 静态方法：直接调用
