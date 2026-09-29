# 学习目标：ThreadPoolExecutor线程池
#
# ThreadPoolExecutor：IO密集型用线程池
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * n

# 线程池：适合 IO 密集型任务
with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(task, [1, 2, 3])
print(list(results))
