# sorted(可迭代,key=函数,reverse=True)排序
nums = [30, 10, 20]
print(sorted(nums))               # [10, 20, 30]
print(sorted(nums, reverse=True))  # [30, 20, 10]

# key 按什么排
words = ['python', 'sql', 'java']
print(sorted(words, key=len))   # 按长度排
