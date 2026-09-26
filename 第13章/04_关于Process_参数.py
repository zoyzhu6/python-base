# Process参数：args位置传参，kwargs关键字传参
from multiprocessing import Process

def task(a, b, msg='默认'):
    print(a, b, msg)

if __name__ == '__main__':
    # args 位置传参，kwargs 关键字传参
    p = Process(target=task, args=(1, 2), kwargs={'msg': 'hi'})
    p.start()
