# 实例属性：每个实例独有，self.属性
class Person:
    def __init__(self, name):
        self.name = name   # 实例属性

p1 = Person('张三')
p2 = Person('李四')
print(p1.name)   # 张三
# Person.name    # ❌ 类访问不了实例属性
