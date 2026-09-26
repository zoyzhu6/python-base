# 通用操作：in判断元素是否存在，list/tuple/set互相转换
print('张三' in {'张三': 72})    # True（判断 key）
print(20 in [10, 20, 30])       # True
print('ab' in 'abc')             # True

# list() tuple() set() str() dict() 互相转换
print(list('hello'))   # ['h','e','l','l','o']
