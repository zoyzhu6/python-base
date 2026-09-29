# 学习目标：filter过滤函数
#
# filter(函数,可迭代)：保留True的元素
nums = [10, 20, 30, 40]  # ⭐ 核心语法
result = filter(lambda n: n > 20, nums)  # ⭐ 匿名函数
print(list(result))   # [30, 40]
