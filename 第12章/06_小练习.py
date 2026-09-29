# 学习目标：文件操作练习
#
# 练习：统计单词频率
from collections import Counter  # ⭐ 从模块导入  # ⭐ 核心语法

with open('test.txt', 'r', encoding='utf-8') as f:
    words = f.read().split()

print(Counter(words).most_common(5))
