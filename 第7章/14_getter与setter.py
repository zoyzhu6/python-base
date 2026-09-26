# @property：把方法变成属性访问
#
# ⚠️ Java vs Python 差异：
#   Java：private int age; getAge() setAge(int age)
#   Python：@property 装饰器，调用时像属性一样
#
#   Java：p.setAge(20);
#   Python：p.age = 20  ← 像赋值，实际调 setter

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):           # getter
        return self._age

    @age.setter
    def age(self, value):    # setter
        if value < 0:
            print('年龄不能为负')
            return
        self._age = value

p = Person(18)
print(p.age)    # 像属性，不是方法 p.age()
p.age = -5      # 像赋值，实际调 setter
