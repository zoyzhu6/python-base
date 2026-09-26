# @property把方法变属性访问，@age.setter赋值校验
class Person:
    def __init__(self, age):
        self._age = age

    # @property：把方法变成属性来访问，做 get
    @property
    def age(self):
        return self._age

    # @age.setter：赋值时做校验
    @age.setter
    def age(self, value):
        if value < 0:
            print('年龄不能为负')
            return
        self._age = value

p = Person(18)
print(p.age)    # 像属性一样调用，不是方法
p.age = -5      # 触发 setter 校验
