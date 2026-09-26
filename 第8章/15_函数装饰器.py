# 装饰器：不修改原函数加额外功能
def log(func):
    def wrapper(*args, **kwargs):
        print('开始调用')
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

print(add(1, 2))   # 先打印"开始调用"，再输出3
