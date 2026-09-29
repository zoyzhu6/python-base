# 学习目标：全局变量局部变量，global声明
#
# 全局/局部变量
#
# ⚠️ Java vs Python 差异：
#   Java：直接用
#   Python：函数内修改全局变量必须加 global
# 全局变量 vs 局部变量
a = 100   # 全局变量
b = 200

def test():
    c = '尚硅谷'   # 局部变量，函数外访问不到
    global a       # 声明：要修改全局变量 a
    a = 300
    print(a, b, c)

test()
print(a)   # 300（被函数改了）
# print(c)  # ❌ c 是局部变量，函数外访问不到
