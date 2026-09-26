# in 判断元素存在
#
# ⚠️ Java vs Python 差异：
#   Java：list.contains("a") map.containsKey("a")
#   Python："a" in list   ← 统一用 in
print('张三' in {'张三': 72})    # True（判断 key）
print(20 in [10, 20, 30])       # True
print('ab' in 'abc')             # True

# list() tuple() set() str() dict() 互相转换
print(list('hello'))   # ['h','e','l','l','o']
