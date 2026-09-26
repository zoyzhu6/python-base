# 鸭子类型：不看类型看有没有方法
class Dog:
    def speak(self): print('汪汪')

class Computer:
    def speak(self): print('滋滋')

def make_sound(x):
    x.speak()   # 只要有 speak 方法就行

make_sound(Dog())
make_sound(Computer())
