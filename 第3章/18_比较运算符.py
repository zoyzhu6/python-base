# 学习目标：== != > < >= <=，注意==比内容
#
# 比较运算符：== != > < >= <=
#
# ⚠️ Java vs Python 差异：
#   ❌ Java：== 比对象地址，equals() 比内容
#   ✅ Python：== 直接比内容，is 比地址
#   ❌ Java：if (a == b) 比的是地址
#   ✅ Python：if a == b 比的是内容

#
# ⚠️ Java vs Python 差异：
#   Java：== 比对象地址，equals() 比内容
#   Python：== 直接比内容（内部调 __eq__）
# == != > < >= <=  返回 True / False
print(5 == '5')   # False（类型不同）  # ⭐ 核心语法
print(9 > 7)      # True

# 字符串比较：按 Unicode 编码逐位比
print('abc' < 'xyz')   # True
