# 综合案例：答题闯关
#
# for/else：循环正常结束走 else，break 不走（Python独有）
# 答题闯关：3关，每关3次机会，输入q退出
print('🏆答题闯关（输入q退出）')
questions = [
    ('Python输出函数？', 'print'),
    ('逻辑并且关键字？', 'and'),
    ('编译型还是解释型？', '解释型'),
]
tries = 3
for q, a in questions:
    for _ in range(tries):
        ans = input(q + '：')
        if ans == a:
            print('✅正确')
            break
        elif ans == 'q':
            print('退出')
            exit()
    else:
        print(f'❌失败，答案：{a}')
        exit()
print('🎉全部通关')
