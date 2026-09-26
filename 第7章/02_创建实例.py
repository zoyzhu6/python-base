# 创建实例：类名()，实例.属性访问
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 类名() 创建实例
p1 = Person('张三', 18)
p2 = Person('李四', 22)

# 实例.属性 访问
print(p1.name, p1.age)

# __dict__ 查看实例所有属性
print(p1.__dict__)
