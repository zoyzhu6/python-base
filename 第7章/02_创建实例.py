# 学习目标：类名()创建实例，没有new关键字
#
# 创建实例：类名()，不需要 new 关键字
#
# ⚠️ Java vs Python 差异：
#   ❌ Java思维：写两个 __init__ 重载
#   ✅ Python：用默认值
#   ❌ Java：Person p = new Person("张三", 18);
#   ✅ Python：p = Person("张三", 18)

#
# ⚠️ Java vs Python 差异：
#   Java：Person p = new Person("张三", 18);
#   Python：p = Person("张三", 18)    ← 没有 new！
#
# ⚠️ 容易踩的坑：
#   - Python 没有重载！不要写两个 __init__，用默认值
#   - 实例属性直接 . 属性访问，没有 getter/setter 也能访问

class Person:  # ⭐ 定义类
    def __init__(self, name, age=0):   # age 不传默认0，相当于Java的重载  # ⭐ 类方法
        self.name = name
        self.age = age

# 创建实例（没有 new）
p1 = Person('张三', 18)
p2 = Person('李四')          # age 用默认值0

# 实例.属性 直接访问（Java 需要 getter）
print(p1.name, p1.age)

# __dict__ 查看实例所有属性（Java 没有这个）
print(p1.__dict__)
