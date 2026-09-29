# 学习目标：terminate强制终止
#
# terminate 强制终止
from multiprocessing import Process
import time

def task():
    time.sleep(10)
    print('不会执行')

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.terminate()   # 强制终止子进程
