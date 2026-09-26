# 九九乘法表
#
# print(end='\t') 不换行，和 Java 的 System.out.print() 一样
# 外层行 1-9，内层列 1-行号
for row in range(1, 10):
    for col in range(1, row + 1):
        print(f'{col}*{row}={col*row}', end='\t')
    print()   # 换行
