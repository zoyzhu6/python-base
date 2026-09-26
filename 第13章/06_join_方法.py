# join()：等子进程结束再继续
from multiprocessing import Process
import time

def task():
    time.sleep(1)
    print('子进程完成')

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()   # 主进程等 p 结束再往下走
    print('主进程结束')
