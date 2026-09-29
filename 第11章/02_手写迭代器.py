# 学习目标：__iter__ __next__实现迭代器
#
# 类实现__iter__和__next__就是迭代器
class Count:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i

for i in Count(3):
    print(i)   # 1 2 3
