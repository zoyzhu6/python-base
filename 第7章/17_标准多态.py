# 学习目标：多态同名方法不同行为
#
# 多态：同名方法不同对象不同行为
#
# ⚠️ Java vs Python 差异：
#   和 Java 类似，但 Python 更灵活（不检查类型）

class Dog:
    def speak(self): print('汪汪')

class Cat:
    def speak(self): print('喵喵')

def make_sound(animal):
    animal.speak()   # 不关心类型，只要有 speak 方法

make_sound(Dog())
make_sound(Cat())
