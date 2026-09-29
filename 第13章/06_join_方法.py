# 学习目标：join等待子进程
#
# join 等待，和 Java Thread.join() 一样
from multiprocessing import Process  # ⭐ 从模块导入  # ⭐ 核心语法
import time  # ⭐ 导入模块

def task():
    time.sleep(1)
    print('子进程完成')

if __name__ == '__main__':  # ⭐ 程序入口
    p = Process(target=task)
    p.start()
    p.join()   # 主进程等 p 结束再往下走
    print('主进程结束')
