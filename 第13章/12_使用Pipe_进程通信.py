# 学习目标：Pipe双向通信
#
# Pipe 双向通信
from multiprocessing import Process, Pipe  # ⭐ 从模块导入  # ⭐ 核心语法

# Pipe 管道：两个进程双向通信
def sender(conn):
    conn.send('你好')

if __name__ == '__main__':  # ⭐ 程序入口
    parent_conn, child_conn = Pipe()
    p = Process(target=sender, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # 你好
