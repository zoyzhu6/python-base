# 列表常用方法
#
# ⚠️ Java vs Python 差异：
#   sort() 改原列表，sorted() 返回新列表
#   Java：Collections.sort(list)
nums = [10, 20, 30, 20, 10]

# index(值)：第一次出现的下标
print(nums.index(20))   # 1

# count(值)：出现次数
print(nums.count(10))   # 2

# reverse()：反转（改原列表）
nums.reverse()

# sort()：排序，reverse=True 降序
nums.sort()
nums.sort(reverse=True)
print(nums)
