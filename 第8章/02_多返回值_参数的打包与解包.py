# 学习目标：多返回值自动打包元组，解包赋值
#
# 多返回值自动打包元组，*args/**kwargs打包解包
def calc(a, b):  # ⭐ 核心语法
    return a + b, a - b

r1, r2 = calc(10, 3)   # 解包
print(r1, r2)

# *args 打包位置参数成元组，**kwargs 打包关键字参数成字典
def show(*args, **kwargs):
    print(args, kwargs)

show(1, 2, name='张三')   # (1, 2) {'name': '张三'}
