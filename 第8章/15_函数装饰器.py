# 学习目标：@装饰器给函数加功能
#
# 装饰器：不修改原函数加额外功能
def log(func):  # ⭐ 核心语法
    def wrapper(*args, **kwargs):
        print('开始调用')
        return func(*args, **kwargs)
    return wrapper

@log  # ⭐ 装饰器
def add(a, b):
    return a + b

print(add(1, 2))   # 先打印"开始调用"，再输出3
