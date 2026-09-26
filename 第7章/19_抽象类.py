# 抽象类：不能实例化，子类必须实现抽象方法
#
# ⚠️ Java vs Python 差异：
#   Java：abstract class Shape { abstract double area(); }
#   Python：继承 ABC + @abstractmethod 装饰器

from abc import ABC, abstractmethod

class Shape(ABC):           # 继承 ABC 就是抽象类
    @abstractmethod
    def area(self):         # 子类必须实现
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):         # 必须实现
        return 3.14 * self.r ** 2

print(Circle(5).area())
