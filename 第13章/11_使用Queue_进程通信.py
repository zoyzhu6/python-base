# 学习目标：生产者消费者模型
#
# Queue 生产者消费者
from multiprocessing import Process, Queue  # ⭐ 从模块导入  # ⭐ 核心语法

def producer(q):
    q.put('数据')

def consumer(q):
    print(q.get())

if __name__ == '__main__':  # ⭐ 程序入口
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start(); p2.start()
    p1.join(); p2.join()
