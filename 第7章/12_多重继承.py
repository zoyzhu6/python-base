# 学习目标：多继承，一个类继承多个父类
#
# 多重继承：一个类继承多个父类
#
# ⚠️ Java vs Python 差异：
#   Java：class A extends B, C  ← 不支持！只能单继承
#   Python：class C(A, B):      ← 支持多继承
#
#   方法查找顺序按 __mro__（从左到右）

class A:
    def hello(self): print('A')

class B:
    def hi(self): print('B')

class C(A, B):   # 同时继承 A 和 B
    pass

c = C()
c.hello()   # A 的
c.hi()      # B 的
