# 学习目标：递归求阶乘
#
# 递归求阶乘
#
# ⚠️ 和 Java 一样
def factorial(num):  # ⭐ 核心语法
    if num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(6))   # 720
