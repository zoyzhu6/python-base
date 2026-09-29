# 学习目标：Thread创建线程
#
# Thread创建线程，共享内存
from threading import Thread
import time

def task(name):
    print(f'{name} 开始')
    time.sleep(1)
    print(f'{name} 结束')

# 线程：同进程内轻量级执行单元，共享内存
t = Thread(target=task, args=('线程1',))
t.start()
t.join()
