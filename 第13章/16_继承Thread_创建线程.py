# 继承Thread重写run方法
from threading import Thread

class MyThread(Thread):
    def run(self):
        print('自定义线程')

t = MyThread()
t.start()
t.join()
