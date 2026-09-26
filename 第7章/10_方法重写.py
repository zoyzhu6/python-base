# 方法重写：子类定义同名方法覆盖父类
class Person:
    def speak(self):
        print('人在说话')

class Student(Person):
    # 重写父类方法
    def speak(self):
        super().speak()   # 还可以调父类的
        print('学生在说话')

s = Student()
s.speak()
