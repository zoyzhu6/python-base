# 嵌套循环
#
# ⚠️ 和 Java 一样
# 外层30天，内层每天3组
for day in range(1, 31):
    print(f'第{day}天')
    for group in range(1, 4):
        print(f'  第{group}组')
