# 学习目标：tuple元组，不可变列表
#
# 元组 tuple：不可变
#
# ⚠️ Java vs Python 差异：
#   Java：没有元组！Java 用 List.of() 或 record
#   Python：(10, 20, 30)  ← 不可变列表
t = (10, 20, 30, 20)
print(t[0])
print(t.count(20))

# 只有一个元素必须加逗号
t2 = (18,)

# 元组不可改，但里面的列表可以改
t3 = (10, 20, [30, 40])
t3[2][0] = 99
print(t3)
