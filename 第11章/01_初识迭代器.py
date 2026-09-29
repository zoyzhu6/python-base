# 学习目标：iter() next()迭代器
#
# 迭代器：iter()创建，next()取下一个
# 迭代器：记录当前位置，每次 next() 取下一个
nums = [1, 2, 3]
it = iter(nums)   # 转成迭代器
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
# next(it)        # StopIteration 报错
