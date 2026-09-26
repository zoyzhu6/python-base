# Queue：进程间通信，先进先出
from multiprocessing import Queue

# Queue 进程间通信：先进先出
q = Queue()
q.put(1)      # 放
q.put(2)
print(q.get())   # 1（先放先取）
print(q.get())   # 2
