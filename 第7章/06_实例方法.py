# 学习目标：实例方法第一个参数self
#
# 实例方法：第一个参数 self，操作实例属性
#
# ⚠️ Java vs Python 差异：
#   就是普通成员方法，和 Java 最像的部分
#   唯一区别：self 要手动写

class Person:  # ⭐ 定义类  # ⭐ 核心语法
    def __init__(self, name):  # ⭐ 类方法
        self.name = name

    def speak(self):  # ⭐ 类方法
        print(f'我是{self.name}')

p = Person('张三')
p.speak()
