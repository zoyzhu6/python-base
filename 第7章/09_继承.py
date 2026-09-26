# 继承：class 子类(父类)
#
# ⚠️ Java vs Python 差异：
#   Java：class Student extends Person { ... }
#   Python：class Student(Person): ...
#
#   super() 调用父类构造，和 Java 类似：
#   Java：super(name, age);
#   Python：super().__init__(name, age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, sid):
        super().__init__(name, age)   # 调父类构造
        self.sid = sid

s = Student('张三', 18, '001')
print(s.name, s.sid)
