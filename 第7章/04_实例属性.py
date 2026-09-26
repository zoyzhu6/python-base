# 实例属性：每个实例独有
#
# ⚠️ Java vs Python 差异：
#   Java：类里先声明 private String name; 构造方法里 this.name = name;
#   Python：不需要提前声明！在 __init__ 里 self.name = name 就是声明+赋值
#
# ⚠️ 容易踩的坑：
#   - Java 类里没声明的属性不能用；Python 里 __init__ 外也能随便加属性
#   - 不同实例可以有不同的属性（p1有address，p2没有）

class Person:
    def __init__(self, name):
        self.name = name   # 没有提前声明，直接赋值就是声明

p1 = Person('张三')
p2 = Person('李四')

p1.address = '北京'   # 运行时随便加属性，Java做不到
print(p1.name)
# print(p2.address)  # ❌ p2 没有这个属性
