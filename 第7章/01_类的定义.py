# 类定义：class 类名: 大驼峰命名（和Java一样）
#
# ⚠️ Java vs Python 差异：
#   Java：public class Person { ... }
#   Python：class Person: ...   没有 public/private 关键字
#
# __init__ 相当于 Java 的构造方法，但：
#   - Python 没有重载！写两个 __init__ 后面的会覆盖前面的
#   - 要实现多种传参方式，用默认值
#   - self 必须写，相当于 Java 的 this，但要手动写出来

class Person:
    # __init__ 构造方法：创建实例时自动调用
    def __init__(self, name, age):
        self.name = name   # self.name = 值，相当于 this.name = name
        self.age = age
