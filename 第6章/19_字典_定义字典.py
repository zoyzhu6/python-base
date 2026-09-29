# 学习目标：dict字典键值对，相当于Java的HashMap
#
# 字典 dict：键值对
#
# ⚠️ Java vs Python 差异：
#   Java：Map<String,Integer> map = new HashMap<>();
#   Python：d = {"张三": 72}   ← 大括号，key:value
d = {'张三': 72, '李四': 60, '王五': 85}  # ⭐ 核心语法

# key 重复时后面的覆盖前面
d2 = {'张三': 72, '张三': 99}
print(d2)   # {'张三': 99}

# 空字典
empty = {}

# 嵌套字典
students = {
    1: {'name': '张三', 'score': 88},
    2: {'name': '李四', 'score': 92}
}
print(students[1]['name'])
