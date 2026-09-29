# 学习目标：类实现装饰器
#
# 类装饰器：实现__call__的类
class Log:  # ⭐ 定义类
    def __init__(self, msg):
        self.msg = msg
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(self.msg)
            return func(*args, **kwargs)
        return wrapper

@Log('开始')  # ⭐ 装饰器
def add(a, b):
    return a + b

print(add(1, 2))
