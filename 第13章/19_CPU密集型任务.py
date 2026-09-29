# 学习目标：CPU密集型用多进程
#
# CPU密集型→多进程
from concurrent.futures import ProcessPoolExecutor  # ⭐ 从模块导入

def heavy(n):
    return sum(i*i for i in range(n))

if __name__ == '__main__':  # ⭐ 程序入口
    with ProcessPoolExecutor() as pool:
        print(list(pool.map(heavy, [10000]*4)))
