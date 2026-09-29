# 学习目标：terminate强制终止
#
# terminate 强制终止
from multiprocessing import Process  # ⭐ 从模块导入  # ⭐ 核心语法
import time  # ⭐ 导入模块

def task():
    time.sleep(10)
    print('不会执行')

if __name__ == '__main__':  # ⭐ 程序入口
    p = Process(target=task)
    p.start()
    p.terminate()   # 强制终止子进程
