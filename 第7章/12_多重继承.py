# 多重继承：一个类继承多个父类
class A:
    def hello(self): print('A')

class B:
    def hi(self): print('B')

class C(A, B):   # 同时继承 A 和 B
    pass

c = C()
c.hello()   # A 的方法
c.hi()      # B 的方法
