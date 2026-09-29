# 学习目标：for k,v in d.items()遍历
#
# 字典遍历
#
# ⚠️ Java vs Python 差异：
#   Java：for (Map.Entry<String,Integer> e : map.entrySet())
#   Python：for k, v in d.items():   ← 解包
d = {'张三': 72, '李四': 60}

# 直接遍历默认拿 key
for key in d:
    print(key, d[key])

# items() 同时拿 key 和 value
for k, v in d.items():
    print(k, v)
