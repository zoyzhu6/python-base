# 字典遍历：默认拿key，items()拿key和value
d = {'张三': 72, '李四': 60}

# 直接遍历默认拿 key
for key in d:
    print(key, d[key])

# items() 同时拿 key 和 value
for k, v in d.items():
    print(k, v)
