# 字符串格式化：f-string（推荐）、%占位符、+拼接
name = '张三'
age = 18

# f-string（推荐）
info = f'我叫{name}，年龄{age}'
print(info)

# % 占位符（老式）
info2 = '我叫%s，年龄%d' % (name, age)

# + 拼接（不推荐）
info3 = '我叫' + name + '，年龄' + str(age)
