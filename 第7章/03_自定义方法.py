# 实例方法：第一个参数self，用实例调用
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法：第一个参数必须是 self（调用者自己）
    def speak(self, msg):
        print(f'我叫{self.name}，{msg}')

p1 = Person('张三', 18)
p1.speak('你好')   # self 自动传入 p1
