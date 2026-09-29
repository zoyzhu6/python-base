# 学习目标：ProcessPoolExecutor进程池
#
# ProcessPoolExecutor：自动管理多进程
from concurrent.futures import ProcessPoolExecutor  # ⭐ 从模块导入

def task(n):
    return n * n

if __name__ == '__main__':  # ⭐ 程序入口
    # 进程池：自动管理多个进程
    with ProcessPoolExecutor(max_workers=4) as pool:
        results = pool.map(task, [1, 2, 3, 4])
    print(list(results))   # [1, 4, 9, 16]
