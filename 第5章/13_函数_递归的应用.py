# 递归求阶乘
#
# ⚠️ 和 Java 一样
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(6))   # 720
