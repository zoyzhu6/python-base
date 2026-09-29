# 学习目标：继承Process重写run
#
# 继承 Process 重写 run
from multiprocessing import Process  # ⭐ 从模块导入

class MyProcess(Process):  # ⭐ 定义类
    def run(self):   # 重写 run 方法
        print('自定义进程')

if __name__ == '__main__':  # ⭐ 程序入口
    p = MyProcess()
    p.start()
