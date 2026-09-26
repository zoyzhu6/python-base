# object是所有类的顶层父类
class Person: pass   # 等价 class Person(object):

p = Person()
print(p.__dict__)   # 对象自己的属性
print(dir(p))       # 对象能访问的所有东西（含继承的）
