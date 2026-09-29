# 学习目标：os模块目录操作
#
# os模块：getcwd/mkdir/rmdir/listdir
import os  # ⭐ 导入模块  # ⭐ 核心语法
print(os.getcwd())        # 当前目录
os.mkdir('new_dir')      # 创建目录
os.rmdir('new_dir')       # 删除空目录
print(os.listdir('.'))    # 列出目录内容
