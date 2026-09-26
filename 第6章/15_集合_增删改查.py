# 集合增删
#
# ⚠️ 和 Java HashSet 类似
s = {10, 20, 30}

# add 添加 / update 批量添加
s.add(40)
s.update([50, 60])

# remove 删除（不存在报错）/ discard 删除（不报错）
s.remove(20)
s.discard(99)

# pop 随机删一个
s.pop()
print(s)
