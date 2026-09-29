# 学习目标：所有类默认继承object
#
# 所有类默认继承 object
#
# ⚠️ Java vs Python 差异：
#   Java：所有类继承 Object（隐式）
#   Python：所有类继承 object（隐式）
#
#   两边类似，Python 里 class Person: 等价 class Person(object):

class Person: pass

p = Person()
print(p.__dict__)   # 实例自己的属性
print(dir(p))       # 所有能访问的方法（含继承的）
