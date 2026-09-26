# 解包传参：*列表/元组 拆成多个位置参数
def test(*args):
    print(args)

nums = [10, 20, 30]
# 调用时 *列表/元组：解包成多个位置参数
test(*nums)   # 等价 test(10, 20, 30)
