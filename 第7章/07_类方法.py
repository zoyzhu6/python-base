# 学习目标：@classmethod第一个参数cls
#
# 类方法：@classmethod，第一个参数 cls
#
# ⚠️ Java vs Python 差异：
#   Java：public static void addCount() { ... }
#   Python：@classmethod / def add_count(cls): ...
#
#   cls 相当于 Java 的类本身，用来操作类属性

class Person:  # ⭐ 定义类
    count = 0

    @classmethod
    def add_count(cls):   # cls 自动传入类本身  # ⭐ 类方法
        cls.count += 1

Person.add_count()
print(Person.count)   # 1
