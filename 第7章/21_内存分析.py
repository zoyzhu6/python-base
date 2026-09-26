# id() 看内存地址
#
# ⚠️ Java vs Python 差异：
#   Java：== 比较基本类型是值，比较对象是地址
#   Python：== 比较内容，is 比较地址
#
#   a == b   内容相等？
#   a is b   是同一个对象吗？

a = [1, 2, 3]
b = a
print(a is b)   # True（同一个对象）

a[0] = 99
print(b[0])    # 99（b 也变了）
