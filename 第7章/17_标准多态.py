# 多态：同名方法不同对象不同行为
class Dog:
    def speak(self): print('汪汪')

class Cat:
    def speak(self): print('喵喵')

def make_sound(animal):
    animal.speak()   # 不关心是什么动物，只要会 speak

make_sound(Dog())
make_sound(Cat())
