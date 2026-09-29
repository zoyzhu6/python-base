# 学习目标：set集合，不无序不重复
#
# 集合 set：不重复
#
# ⚠️ Java vs Python 差异：
#   Java：Set<Integer> set = new HashSet<>();
#   Python：{10, 20, 30}   ← 大括号
s = {10, 20, 20, 30, 30, 40}  # ⭐ 核心语法
print(s)   # {10, 20, 30, 40}

# 空集合用 set()，{} 是空字典
empty = set()

# frozenset 是不可变集合
fs = frozenset([1, 2, 3])
