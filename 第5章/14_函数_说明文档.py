# 学习目标：三引号写文档字符串help()查看
#
# 文档字符串
#
# ⚠️ Java vs Python 差异：
#   Java：/** javadoc */
#   Python：三引号写在函数开头，help() 查看
# 文档字符串：写在函数开头，用 help() 可以查看
def add(n1, n2):  # ⭐ 核心语法
    """计算两个数相加"""
    return n1 + n2

help(add)
