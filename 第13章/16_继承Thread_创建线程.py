# 继承 Thread 重写 run，和 Java 一样
from threading import Thread

class MyThread(Thread):
    def run(self):
        print('自定义线程')

t = MyThread()
t.start()
t.join()
