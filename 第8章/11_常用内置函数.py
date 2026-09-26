# 内置函数：abs/round/max/min/sum/zip/all/any
print(abs(-5))        # 5 绝对值
print(round(3.7))     # 4 四舍五入
print(max(1, 5, 3))   # 5
print(min(1, 5, 3))   # 1
print(sum([1,2,3]))    # 6

# zip：多个序列一一配对
names = ['张三', '李四']
ages = [18, 20]
print(list(zip(names, ages)))   # [('张三',18), ('李四',20)]

# all 全真才真 / any 有真就行
print(all([1, 2, 3]))   # True
print(any([0, '', 1]))  # True
