# 类方法：@classmethod，第一个参数cls，操作类属性
class Person:
    count = 0

    # @classmethod 类方法：第一个参数 cls（类本身），操作类属性
    @classmethod
    def add_count(cls):
        cls.count += 1

Person.add_count()
print(Person.count)   # 1
