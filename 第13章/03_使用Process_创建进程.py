# 学习目标：Process创建子进程
#
# Process创建子进程，start()启动join()等待
from multiprocessing import Process  # ⭐ 从模块导入  # ⭐ 核心语法
import time  # ⭐ 导入模块

def task(name):
    print(f'{name} 开始')
    time.sleep(1)
    print(f'{name} 结束')

if __name__ == '__main__':  # ⭐ 程序入口
    p = Process(target=task, args=('子进程',))
    p.start()   # 启动
    p.join()    # 等子进程结束
