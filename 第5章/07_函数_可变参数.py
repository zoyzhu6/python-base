# 可变参数：*args **kwargs
#
# ⚠️ Java vs Python 差异：
#   Java：int... nums 可变参数，只能放最后
#   Python：*args 打包成元组，**kwargs 打包成字典
# *args：收集多余的位置参数，打包成元组
def test1(*args):
    print(args)

test1('张三', '男', 18, 172)   # args = ('张三', '男', 18, 172)


# **kwargs：收集多余的关键字参数，打包成字典
def test2(**kwargs):
    print(kwargs)

test2(name='张三', gender='男', age=18)  # kwargs = {'name': '张三', 'gender': '男', 'age': 18}


# 混用：位置参数 + *args + 默认值 + **kwargs
def test3(a, b, *args, c='尚硅谷', **kwargs):
    print(a, b, c, args, kwargs)

test3('张三', '男', '抽烟', '喝酒', age=18, height=172)
# a='张三', b='男', args=('抽烟','喝酒'), c='尚硅谷', kwargs={'age':18,'height':172}
