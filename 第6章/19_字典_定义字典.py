# 字典 dict：键值对用{}，key唯一，key不可变
d = {'张三': 72, '李四': 60, '王五': 85}

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
