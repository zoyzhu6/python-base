# 内置函数：len max min sum
#
# ⚠️ Java vs Python 差异：
#   Java：list.size()
#   Python：len(list)   ← 函数，不是方法
nums = [10, 20, 30, 40, 50]

# sorted()：返回新列表，不改原列表
print(sorted(nums, reverse=True))

# len() 长度  max() 最大  min() 最小  sum() 求和
print(len(nums), max(nums), min(nums), sum(nums))
