# 逻辑运算符：and两边都真 or一边真就真 not取反，支持短路
# and：两边都真才真；or：一边真就真；not：取反
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# 短路：and 左边假就不看右边；or 左边真就不看右边
print(False and 1/0)    # False（不报错）
print(True or 1/0)       # True（不报错）
