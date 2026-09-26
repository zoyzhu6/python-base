# while 循环
#
# ⚠️ Java vs Python 差异：
#   Java：while (n <= 10) { n++; }
#   Python：while n <= 10:  没有 n++，用 n += 1
# while 条件：条件为 True 就一直循环
n = 1
while n <= 10:
    print(f'第{n}次')
    n += 1
