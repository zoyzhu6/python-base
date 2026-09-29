# 学习目标：True/False首字母大写，0空串None是False
#
# 布尔类型：True / False
#
# ⚠️ Java vs Python 差异：
#   ❌ Java：if (flag == true)
#   ✅ Python：if flag:  ← 直接判断，不用 == true
#   ❌ Java：true / false 全小写
#   ✅ Python：True / False 首字母大写！
#   0、空串""、None 都是 False，其他都是 True

#
# ⚠️ Java vs Python 差异：
#   Java：true / false 全小写
#   Python：True / False 首字母大写！
#
#   0、空串""、None 都是 False，其他都是 True
# True / False（首字母大写）
a = True  # ⭐ 核心语法
b = 5 > 3     # True

# bool() 转布尔：0、空串、None 是 False，其他是 True
print(bool(0))       # False
print(bool(''))      # False
print(bool('hello')) # True
