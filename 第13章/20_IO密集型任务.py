# 学习目标：IO密集型用多线程
#
# IO密集型→多线程
from concurrent.futures import ThreadPoolExecutor  # ⭐ 从模块导入  # ⭐ 核心语法
import time  # ⭐ 导入模块

def fetch(url):
    time.sleep(1)   # 模拟网络等待
    return f'{url} 完成'

with ThreadPoolExecutor() as pool:
    print(list(pool.map(fetch, ['a', 'b', 'c'])))
