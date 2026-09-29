# 学习目标：if/elif/else多分支
#
# if/elif/else 多分支
#
# ⚠️ Java vs Python 差异：
#   Java：else if
#   Python：elif   ← 连写
# if / elif / else：从上到下匹配，命中就停
age = int(input('请输入年龄：'))
if age <= 10:
    print('幼儿')
elif age <= 18:
    print('青少年')
elif age <= 30:
    print('青年')
else:
    print('老年')
