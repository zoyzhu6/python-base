# 练习：统计单词频率
from collections import Counter

with open('test.txt', 'r', encoding='utf-8') as f:
    words = f.read().split()

print(Counter(words).most_common(5))
