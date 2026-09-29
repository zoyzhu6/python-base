# 学习目标：for遍历循环，range()生成序列
#
# for 循环
#
# ⚠️ Java vs Python 差异：
#   Java：for (int i = 0; i < 10; i++) { ... }
#   Python：for i in range(10): ...   ← 遍历，不是C风格for
#
#   range(1, 11) 含1不含11
# for 变量 in range(起, 止)：遍历数字范围（含起不含止）
for n in range(1, 11):  # ⭐ 核心语法
    print(n)

# for 遍历字符串
for ch in 'abc':
    print(ch)
