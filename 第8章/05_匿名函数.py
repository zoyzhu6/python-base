# 学习目标：lambda匿名函数
#
# lambda一行匿名函数
add = lambda x, y: x + y
print(add(1, 2))   # 3

# 常用于当高阶函数的参数
nums = [10, 20, 30]
print(list(map(lambda n: n * 2, nums)))
