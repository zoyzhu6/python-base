# 学习目标：PID进程号
#
# 进程PID查看
import os  # ⭐ 导入模块
print(f'当前进程PID: {os.getpid()}')
print(f'父进程PID: {os.getppid()}')
