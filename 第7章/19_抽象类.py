# 抽象类：ABC+abstractmethod，不能实例化，子类必须实现
from abc import ABC, abstractmethod

# 抽象类：不能实例化，只定规范
class Shape(ABC):
    @abstractmethod
    def area(self):   # 子类必须实现
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):   # 必须实现
        return 3.14 * self.r ** 2

print(Circle(5).area())
