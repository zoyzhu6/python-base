# 高阶函数：参数是函数或返回值是函数
def log(func, text):
    print(func(text))

def info(msg): return f'[INFO] {msg}'
def error(msg): return f'[ERROR] {msg}'

log(info, '保存成功')
log(error, '出错了')
