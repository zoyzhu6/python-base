# 学习目标：鸭子类型不看类型看方法
#
# 鸭子类型：不看类型，看有没有方法
#
# ⚠️ Java vs Python 差异：
#   Java：必须实现同一个接口才能传
#   Python：只要有这个方法就行，不管是什么类
#
#   "如果走起来像鸭子，叫起来像鸭子，那它就是鸭子"

class Dog:  # ⭐ 定义类  # ⭐ 核心语法
    def speak(self): print('汪汪')  # ⭐ 类方法

class Computer:   # 不是动物，但有 speak 方法  # ⭐ 定义类
    def speak(self): print('滋滋')  # ⭐ 类方法

def make_sound(x):
    x.speak()   # 不检查类型，能调就行

make_sound(Dog())
make_sound(Computer())   # Java 里会报错
