# 集合 set：无序不重复用{}，自动去重，空集合用set()
s = {10, 20, 20, 30, 30, 40}
print(s)   # {10, 20, 30, 40}

# 空集合用 set()，{} 是空字典
empty = set()

# frozenset 是不可变集合
fs = frozenset([1, 2, 3])
