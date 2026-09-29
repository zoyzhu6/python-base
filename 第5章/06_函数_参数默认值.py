# 学习目标：默认值参数，相当于Java重载
#
# 默认值参数
#
# ⚠️ Java vs Python 差异：
#   Java：重载实现多个构造方法
#   Python：默认值参数实现，def greet(name, msg="你好")
# 默认值：调用时不传就用默认值
def greet(name, gender, age, height, msg='你好'):  # ⭐ 核心语法
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')
    print(f'我想说：{msg}')

greet('张三', '男', 18, 172)                  # msg 用默认值
greet('张三', '男', 18, 172, 'hello')          # 位置传
greet('张三', '男', 18, 172, msg='hello')     # 关键字传

# print 的 end 参数默认值是 '\n'
print('尚硅谷', end='!!')
