# Pipe 双向通信
from multiprocessing import Process, Pipe

# Pipe 管道：两个进程双向通信
def sender(conn):
    conn.send('你好')

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=sender, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # 你好
