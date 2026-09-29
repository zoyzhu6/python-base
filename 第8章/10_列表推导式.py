# 学习目标：列表推导式[for if]，Python独有
#
# [表达式for变量in可迭代if条件]
nums = [1, 2, 3, 4]  # ⭐ 核心语法

# 每个翻倍
print([n * 2 for n in nums])          # [2, 4, 6, 8]

# 只取大于2的
print([n for n in nums if n > 2])     # [3, 4]

# 字典推导式
print({k: v for k, v in zip(['a','b'], [1,2])})
