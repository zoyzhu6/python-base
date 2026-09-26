# 函数嵌套调用
#
# ⚠️ 和 Java 一样
# 函数嵌套调用：test1 → test2 → test3，再一层层返回
def test1():
    print('进入 test1')
    test2()
    print('退出 test1')

def test2():
    print('进入 test2')
    test3()
    print('退出 test2')

def test3():
    print('进入 test3')
    print('执行 test3')
    print('退出 test3')

test1()
