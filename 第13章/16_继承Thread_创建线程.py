# 学习目标：继承Thread重写run
#
# 继承 Thread 重写 run，和 Java 一样
from threading import Thread  # ⭐ 从模块导入  # ⭐ 核心语法

class MyThread(Thread):  # ⭐ 定义类
    def run(self):
        print('自定义线程')

t = MyThread()
t.start()
t.join()
