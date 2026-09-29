# 学习目标：return返回值，多个值自动打包元组
#
# return 返回值
#
# ⚠️ Java vs Python 差异：
#   ❌ Java：return new Result(a, b)  或写个类
#   ✅ Python：return a, b  ← 自动打包元组
#   r1, r2 = calc(1, 2)  ← 解包

#
# ⚠️ Java vs Python 差异：
#   Java：必须声明返回类型 void/int/String
#   Python：不用声明，return 多个值自动打包成元组
def add(n1, n2):
    return n1 + n2

result = add(100, 200)   # result 拿到返回值
print(result)

# print 没有返回值（返回 None）
# res = print('hello')
# print(res)   # None
