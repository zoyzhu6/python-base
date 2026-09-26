# 闭包：内层函数+记住外层变量
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c = counter()
print(c())   # 1
print(c())   # 2
