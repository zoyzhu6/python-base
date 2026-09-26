# IO密集型→用多线程
from concurrent.futures import ThreadPoolExecutor
import time

def fetch(url):
    time.sleep(1)   # 模拟网络等待
    return f'{url} 完成'

with ThreadPoolExecutor() as pool:
    print(list(pool.map(fetch, ['a', 'b', 'c'])))
