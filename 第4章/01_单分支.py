# 学习目标：if单分支判断，缩进代替大括号
#
# if 单分支
#
# ⚠️ Java vs Python 差异：
#   Java：if (age >= 18) { ... }
#   Python：if age >= 18: ...   ← 没有括号，有冒号，缩进代替大括号
#
#   Python 用缩进表示代码块，不是 {}
# if 条件：条件为 True 才执行
age = int(input('请输入年龄：'))  # ⭐ 核心语法
if age >= 18:
    print('你是成年人')
