# 学习目标：关键字传参，参数名=值，顺序随意
#
# 关键字参数：参数名=值
#
# ⚠️ Java vs Python 差异：
#   Java：只能按顺序传
#   Python：greet(name="张三", age=18)  ← 可以按名字传，顺序随意
# 关键字参数：用 参数名=值 传，顺序随意
def greet(name, gender, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')

greet(name='张三', gender='男', age=18, height=172)
greet(height=172, age=18, gender='男', name='张三')  # 顺序乱也没事
greet('张三', '男', height=172, age=18)              # 位置+关键字混用

# greet(height=172, age=18, '张三', '男')   # ❌ 关键字传了之后不能再位置传
# greet(name='张三', '男', 18, 172)         # ❌ 同上
# greet(name='张三', gender='男', age=18)   # ❌ 少传 height
# greet(name='张三', age=18, age=19)        # ❌ age 传了两次
# greet(name='张三', school='尚硅谷')        # ❌ 没有 school 这个参数
