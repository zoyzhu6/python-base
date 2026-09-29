# 学习目标：函数自己调自己
#
# 递归
#
# ⚠️ 和 Java 一样，但 Python 递归深度有限制（默认1000层）
# 递归：函数自己调用自己，必须有终止条件

# 从大到小：先打印再递归
def welcome(n):
    print(f'你好啊{n}')
    if n > 1:
        welcome(n - 1)

welcome(5)


# 从小到大：先递归再打印
def welcome(n):
    if n > 1:
        welcome(n - 1)
    print(f'你好啊{n}')

welcome(5)
