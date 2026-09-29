# 学习目标：Queue进程通信
#
# Queue 进程通信
from multiprocessing import Queue  # ⭐ 从模块导入

# Queue 进程间通信：先进先出
q = Queue()
q.put(1)      # 放
q.put(2)
print(q.get())   # 1（先放先取）
print(q.get())   # 2
