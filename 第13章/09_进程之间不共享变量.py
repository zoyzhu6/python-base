# 学习目标：多进程独立内存不共享
#
# 进程有独立内存，变量不共享
from multiprocessing import Process

# 进程有独立内存，变量不共享
num = 0
def work():
    global num
    num += 1
    print(f'子进程 num={num}')

if __name__ == '__main__':
    for _ in range(3):
        Process(target=work).start()
    print(f'主进程 num={num}')   # 还是0
