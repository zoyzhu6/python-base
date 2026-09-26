# 函数是对象：可赋值、当参数、当返回值
def welcome():
    print('你好')

f = welcome    # 函数赋值给变量
f()            # 跟调用 welcome 一样

# 函数当返回值
def outer():
    def inner():
        print('inner')
    return inner

outer()()   # 调 outer 返回 inner，再调 inner
