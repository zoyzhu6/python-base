# 学习目标：闭包内层函数记住外层变量
#
# 闭包：内层函数+记住外层变量
def counter():  # ⭐ 核心语法
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c = counter()
print(c())   # 1
print(c())   # 2
