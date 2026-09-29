# 学习目标：f-string格式化输出，最常用
#
# 字符串格式化：f-string 最方便
#
# ⚠️ Java vs Python 差异：
#   Java：String.format("我叫%s", name)  或 "我叫" + name
#   Python：f"我叫{name}"  ← 直接 {} 里放变量，最推荐
name = '张三'  # ⭐ 核心语法
age = 18

# f-string（推荐）
info = f'我叫{name}，年龄{age}'
print(info)

# % 占位符（老式）
info2 = '我叫%s，年龄%d' % (name, age)

# + 拼接（不推荐）
info3 = '我叫' + name + '，年龄' + str(age)
