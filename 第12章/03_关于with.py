# 学习目标：with自动关流try-with-resources
#
# with自动关闭文件
with open('test.txt', 'r', encoding='utf-8') as f:  # ⭐ 核心语法
    content = f.read()
    print(content)
# 出了 with 块自动 close
