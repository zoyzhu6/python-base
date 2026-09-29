# 学习目标：异常往上抛
#
# 异常往上抛，直到被try接住
def func1():  # ⭐ 核心语法
    raise ValueError('出错了')

def func2():
    func1()

try:
    func2()
except ValueError as e:
    print(f'捕获到：{e}')
