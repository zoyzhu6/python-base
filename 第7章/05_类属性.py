# 学习目标：类属性所有实例共享，相当于static
#
# 类属性：类里直接定义，所有实例共享
#
# ⚠️ Java vs Python 差异：
#   Java：static String species = "人类";  ← static 关键字
#   Python：species = "人类"               ← 没有 static，直接写
#
# ⚠️ 容易踩的坑：
#   - p.species = "新" 是给 p 加了个同名实例属性，不是改类属性！
#   - 改类属性要用 类名.属性 = 值

class Person:  # ⭐ 定义类  # ⭐ 核心语法
    species = '人类'   # 类属性（相当于 Java 的 static）

    def __init__(self, name):  # ⭐ 类方法
        self.name = name

p1 = Person('张三')
print(Person.species)   # 类访问
print(p1.species)       # 实例也能访问（自己没有就找类）

p1.species = '新人类'    # 这是给 p1 加了个同名实例属性
print(Person.species)    # 还是"人类"，类属性没变
print(p1.species)       # "新人类"（实例自己的）
