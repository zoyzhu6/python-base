# 学习目标：LEGB作用域规则
#
# 作用域：L本地→E外层→G全局→B内置
x = 'global'

def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print(x)   # local
    inner()

outer()
