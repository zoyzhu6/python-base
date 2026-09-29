# 学习目标：集合常用方法
#
# 集合方法
#
# ⚠️ 和 Java Set 类似
s1 = {10, 20, 30, 40}  # ⭐ 核心语法
s2 = {30, 40, 50, 60}

# difference 差集 / union 并集 / issubset 子集 / isdisjoint 无交集
print(s1.difference(s2))      # {10, 20}
print(s1.union(s2))           # {10,20,30,40,50,60}
print({30,40}.issubset(s1))   # True
print(s1.isdisjoint({99}))    # True
