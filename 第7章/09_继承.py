# 继承：class子类(父类)，super()调父类构造
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, sid):
        super().__init__(name, age)   # 调父类构造
        self.sid = sid               # 子类自己的属性

s = Student('张三', 18, '001')
print(s.name, s.sid)
