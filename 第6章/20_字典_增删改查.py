# 学习目标：字典增删改查 d[key]=value
#
# 字典增删改查
#
# ⚠️ Java vs Python 差异：
#   Java：map.put("a", 1); map.get("a");
#   Python：d["a"] = 1; d["a"];  ← 中括号
d = {'张三': 72, '李四': 60}

# 查：d[key] 不存在会报错；d.get(key, 默认值) 更安全
print(d['张三'])
print(d.get('王五', '不存在'))

# 增/改：d[key] = 值，有就改，没有就加
d['王五'] = 85   # 新增
d['张三'] = 99   # 修改

# 删：pop(key) 返回值，del d[key]
d.pop('李四')

# 清空
# d.clear()
print(d)
