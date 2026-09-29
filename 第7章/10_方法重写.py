# 学习目标：子类重写父类方法
#
# 方法重写：子类定义同名方法覆盖父类
#
# ⚠️ Java vs Python 差异：
#   和 Java 一样，直接写同名方法就是重写
#   super().方法() 调父类的，和 Java 一样

class Person:
    def speak(self):
        print('人在说话')

class Student(Person):
    def speak(self):           # 重写
        super().speak()         # 调父类的
        print('学生在说话')

s = Student()
s.speak()
