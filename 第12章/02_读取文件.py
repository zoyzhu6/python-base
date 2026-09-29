# 学习目标：open().read()读文件
#
# open()读文件，read/readline/readlines
f = open('test.txt', 'r', encoding='utf-8')  # ⭐ 核心语法
content = f.read()      # 全部读
# line = f.readline()   # 读一行
# lines = f.readlines()  # 读所有行成列表
f.close()
print(content)
