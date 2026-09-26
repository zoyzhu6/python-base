# 字符串方法
#
# ⚠️ Java vs Python 差异：
#   Java：s.split(",") s.replace("a","b") s.trim()
#   Python：s.split(",") s.replace("a","b") s.strip()  ← 基本一样
s = 'hello world'
print(s[0])       # h
print(len(s))     # 11

# split 分割成列表 / replace 替换 / count 计数 / strip 去两端空白
print(s.split(' '))          # ['hello', 'world']
print(s.replace('world', 'python'))
print(s.count('l'))           # 3
print('  hi  '.strip())       # 'hi'
