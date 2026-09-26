# 类属性：类里直接定义，所有实例共享
class Person:
    species = '人类'   # 类属性

    def __init__(self, name):
        self.name = name   # 实例属性

p1 = Person('张三')
print(Person.species)   # 类访问
print(p1.species)       # 实例也能访问（自己没有就找类）

p1.species = '新人类'   # 这是给 p1 加了个同名实例属性，不改类
print(Person.species)  # 人类
