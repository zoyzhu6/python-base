# 学习目标：map映射函数
#
# map(函数,可迭代)：每个元素过一遍函数
nums = [10, 20, 30]
result = map(lambda n: n * 2, nums)
print(list(result))   # [20, 40, 60]
