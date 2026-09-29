# 学习目标：reduce归约函数
#
# reduce：不断合并成一个结果
from functools import reduce  # ⭐ 从模块导入  # ⭐ 核心语法
# reduce(函数, 可迭代, 初始值)：不断合并成一个结果
nums = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, nums))   # 10  # ⭐ 匿名函数
