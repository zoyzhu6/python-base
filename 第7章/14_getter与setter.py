# 学习目标：@property装饰器getter setter
#
# @property：把方法变成属性访问
#
# ⚠️ Java vs Python 差异：
#   Java：private int age; getAge() setAge(int age)
#   Python：@property 装饰器，调用时像属性一样
#
#   Java：p.setAge(20);
#   Python：p.age = 20  ← 像赋值，实际调 setter

class Person:  # ⭐ 定义类
    def __init__(self, age):  # ⭐ 类方法
        self._age = age

    @property
    def age(self):           # getter  # ⭐ 类方法
        return self._age

    @age.setter
    def age(self, value):    # setter  # ⭐ 类方法
        if value < 0:
            print('年龄不能为负')
            return
        self._age = value

p = Person(18)
print(p.age)    # 像属性，不是方法 p.age()
p.age = -5      # 像赋值，实际调 setter
