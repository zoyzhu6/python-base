# 学习目标：实例方法第一个参数self
#
# 实例方法：第一个参数 self，操作实例属性
#
# ⚠️ Java vs Python 差异：
#   就是普通成员方法，和 Java 最像的部分
#   唯一区别：self 要手动写

class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'我是{self.name}')

p = Person('张三')
p.speak()
