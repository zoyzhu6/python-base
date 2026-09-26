# 实例方法：操作实例属性的方法
class Person:
    def __init__(self, name):
        self.name = name

    # 实例方法：第一个参数 self，用实例调用
    def speak(self):
        print(f'我是{self.name}')

p = Person('张三')
p.speak()
