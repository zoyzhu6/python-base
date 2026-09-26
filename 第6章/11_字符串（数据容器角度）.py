# 字符串方法：split/replace/count/strip
s = 'hello world'
print(s[0])       # h
print(len(s))     # 11

# split 分割成列表 / replace 替换 / count 计数 / strip 去两端空白
print(s.split(' '))          # ['hello', 'world']
print(s.replace('world', 'python'))
print(s.count('l'))           # 3
print('  hi  '.strip())       # 'hi'
