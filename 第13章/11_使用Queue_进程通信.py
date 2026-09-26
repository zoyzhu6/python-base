# Queue实现生产者消费者模式
from multiprocessing import Process, Queue

def producer(q):
    q.put('数据')

def consumer(q):
    print(q.get())

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start(); p2.start()
    p1.join(); p2.join()
