# 学习目标：type()查看数据类型，万物皆对象
#
# 数据类型：type() 查看
#
# ⚠️ Java vs Python 差异：
#   Java：int / double / String 是基本类型+类
#   Python：int / float / str 都是类，万物皆对象
# type() 查看数据类型
print(type('张三'))   # <class 'str'>  # ⭐ 核心语法
print(type(18))       # <class 'int'>
print(type(65.2))     # <class 'float'>
print(type('18'))     # str（加了引号就是字符串）
