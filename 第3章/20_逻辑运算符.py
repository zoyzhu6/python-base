# 学习目标：and or not，用单词不用符号
#
# 逻辑运算符：and or not
#
# ⚠️ Java vs Python 差异：
#   ❌ Java：if (a && b || !c)
#   ✅ Python：if a and b or not c
#   Python 用单词，不用符号！

#
# ⚠️ Java vs Python 差异：
#   Java：&&  ||  !
#   Python：and  or  not  ← 用单词，不用符号
# and：两边都真才真；or：一边真就真；not：取反
print(True and False)   # False  # ⭐ 核心语法
print(True or False)    # True
print(not True)         # False

# 短路：and 左边假就不看右边；or 左边真就不看右边
print(False and 1/0)    # False（不报错）
print(True or 1/0)       # True（不报错）
