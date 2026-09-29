# 学习目标：daemon守护进程
#
# daemon=True：主进程死它就死
from multiprocessing import Process  # ⭐ 从模块导入
import time  # ⭐ 导入模块

def daemon_task():
    time.sleep(10)
    print('主进程死了就不会执行')

if __name__ == '__main__':  # ⭐ 程序入口
    p = Process(target=daemon_task)
    p.daemon = True   # 守护进程：主进程结束它就死
    p.start()
    time.sleep(1)
    print('主进程结束')
