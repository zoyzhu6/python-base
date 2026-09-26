# 字典方法：keys values items
#
# ⚠️ Java vs Python 差异：
#   Java：map.keySet() map.values() map.entrySet()
#   Python：d.keys() d.values() d.items()
d = {'张三': 72, '李四': 60, '王五': 85}

# keys() 所有键  values() 所有值  items() 所有键值对
print(d.keys())
print(d.values())
print(d.items())
# dict_items([('张三', 72), ('李四', 60), ...])
