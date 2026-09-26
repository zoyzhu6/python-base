# 默认值参数：调用时不传就用默认值
# 默认值：调用时不传就用默认值
def greet(name, gender, age, height, msg='你好'):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')
    print(f'我想说：{msg}')

greet('张三', '男', 18, 172)                  # msg 用默认值
greet('张三', '男', 18, 172, 'hello')          # 位置传
greet('张三', '男', 18, 172, msg='hello')     # 关键字传

# print 的 end 参数默认值是 '\n'
print('尚硅谷', end='!!')
