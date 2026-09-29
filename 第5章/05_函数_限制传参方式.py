# 学习目标：/和*限制传参方式
#
# /和*限制传参
#
# ⚠️ Java 没有这个概念
#   /前只能位置传，*后必须关键字传
# / 前面：只能位置传；/ 和 * 之间：都行；* 后面：必须关键字传
def greet(name, /, gender, *, age, height):  # ⭐ 核心语法
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')


greet('张三', '男', age=18, height=172)          # ✅
greet('张三', gender='男', age=18, height=172)  # ✅

# greet(name='张三', gender='男', age=18, height=172)  # ❌ name 不能关键字传
# greet('张三', '男', 18, height=172)                   # ❌ age 必须关键字传
