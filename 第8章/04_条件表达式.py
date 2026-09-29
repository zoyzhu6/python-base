# 学习目标：三元表达式 if-else写法
#
# 三元表达式
#
# ⚠️ Java vs Python 差异：
#   ❌ Java：String s = age >= 18 ? "成年" : "未成年";
#   ✅ Python：s = "成年" if age >= 18 else "未成年"
#   注意顺序反过来！

age = 21
result = '成年' if age >= 18 else '未成年'
print(result)
