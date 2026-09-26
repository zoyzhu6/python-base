# 生成器：yield的函数，自动实现迭代器
def count(n):
    for i in range(1, n + 1):
        yield i   # 暂停，返回值，下次继续

for i in count(3):
    print(i)   # 1 2 3
