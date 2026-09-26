# Lock 加锁
#
# ⚠️ 和 Java ReentrantLock 类似
from multiprocessing import Process, Lock

# Lock 加锁：防止多个进程同时改同一个资源
def work(lock, n):
    lock.acquire()    # 加锁
    print(f'进程{n} 执行')
    lock.release()    # 释放

if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        Process(target=work, args=(lock, i)).start()
