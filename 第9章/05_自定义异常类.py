# 学习目标：自定义异常继承Exception
#
# 自定义异常：继承Exception
class MyError(Exception):  # ⭐ 定义类
    def __init__(self, msg):
        self.msg = msg

def check(age):
    if age < 18:
        raise MyError('未成年')

try:
    check(15)
except MyError as e:
    print(e.msg)
