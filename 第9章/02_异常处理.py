# try/except/finally：捕获异常
try:
    n = int(input('输入数字：'))
    print(10 / n)
except ValueError:
    print('不是数字')
except ZeroDivisionError:
    print('不能为0')
finally:
    print('结束')
