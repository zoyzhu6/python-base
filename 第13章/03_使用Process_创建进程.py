# Process创建子进程，start()启动join()等待
from multiprocessing import Process
import time

def task(name):
    print(f'{name} 开始')
    time.sleep(1)
    print(f'{name} 结束')

if __name__ == '__main__':
    p = Process(target=task, args=('子进程',))
    p.start()   # 启动
    p.join()    # 等子进程结束
